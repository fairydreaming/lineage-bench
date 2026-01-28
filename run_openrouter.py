#!/usr/bin/env -S python3 -u

import os
import csv
import sys
import argparse
import time
import json
import requests
import hashlib
from tqdm.contrib.concurrent import process_map

DEFAULT_SYSTEM_PROMPT="You are a master of logical thinking. You carefully analyze the premises step by step, take detailed notes and draw intermediate conclusions based on which you can find the final answer to any question."

api_urls = {
    "openrouter": "https://openrouter.ai/api/v1/chat/completions",
    "openai": "https://api.openai.com/v1/chat/completions",
    "zenmux": "https://zenmux.ai/api/v1/chat/completions",
}

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--api", help="API Provider", type=str, default="openrouter", choices=["openrouter", "openai", "zenmux"])
parser.add_argument("-u", "--url", help="OpenAI-compatible API URL", type=str)
parser.add_argument("-m", "--model", help="OpenRouter model name.", required=True)
parser.add_argument("-o", "--output", help="Directory for storing model responses.")
parser.add_argument("-p", "--provider", help="OpenRouter provider name.")
parser.add_argument("-r", "--reasoning", help="Enable reasoning.", action='store_true', default=False)
parser.add_argument("-e", "--effort", help="Reasoning effort (recent OpenAI and xAI models support this).", choices=["low", "medium", "high", "xhigh"])
parser.add_argument("-t", "--threads", help="Number of threads to use.", type=int, default=8)
parser.add_argument("-v", "--verbose", help="Enable verbose output.", action="store_true")
parser.add_argument("-s", "--system-prompt", help="Use given system prompt. By default, the system prompt is not used. When this option is passed without a value, the default system prompt value is used: " + repr(DEFAULT_SYSTEM_PROMPT), const=DEFAULT_SYSTEM_PROMPT, default=None, nargs='?')
parser.add_argument("-T", "--temp", help="Temperature value to use.", type=float)
parser.add_argument("-P", "--top-p", help="top_p sampling parameter.", type=float)
parser.add_argument("-K", "--top-k", help="top_k sampling parameter.", type=int)
parser.add_argument("-n", "--max-tokens", help="Max number of tokens to generate.", type=int)
parser.add_argument("-V", "--verbosity", help="Model verbosity (recent OpenAI models support this).", choices=["low", "medium", "high"])
parser.add_argument("-i", "--retries", help="Max number of API request retries.", type=int, default=5)
args = parser.parse_args()
api_provider = args.api
output_dir = args.output
model_name = args.model
provider_name = args.provider
system_prompt = args.system_prompt
reasoning_enabled = args.reasoning
reasoning_effort = args.effort
num_threads = args.threads
is_verbose = args.verbose
temperature = args.temp
max_tokens = args.max_tokens
verbosity = args.verbosity
top_p = args.top_p
top_k = args.top_k
api_url = args.url if args.url else api_urls[api_provider]
max_retries = args.retries

quiz_reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
csv_writer = csv.writer(sys.stdout)
api_key = os.getenv("OPENROUTER_API_KEY")

if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

def make_request(row):
    global provider_name
    global system_prompt
    global reasoning_effort
    global api_key
    global api_url
    global is_verbose

    problem_size, relation_name, correct_answer, quiz = row

    quiz_id = hashlib.md5(quiz.encode('utf-8')).hexdigest()

    if is_verbose:
        print(f"[{quiz_id}] Processing quiz", file=sys.stderr)

    system_messages=[{"role": "system", "content": system_prompt }]
    messages=[{"role": "user", "content": quiz }]
    if system_prompt is not None:
        messages = system_messages + messages

    request_data = {
        "model": model_name,
        "seed": 42,
        "messages": messages,
    }

    if temperature:
        request_data["temperature"] = temperature;

    if max_tokens:
        request_data["max_tokens"] = max_tokens

    if provider_name:
        request_data["provider"] = { "order": [ provider_name ], "allow_fallbacks": False }

    if api_provider != "openai" and reasoning_enabled:
        request_data["reasoning"] = { "enabled": True }

    if reasoning_effort:
        assert(reasoning_enabled)
        if api_provider != "openai":
            request_data["reasoning"]["effort"] = reasoning_effort
        else:
            request_data["reasoning_effort"] = reasoning_effort

    if verbosity:
        request_data["verbosity"] = verbosity

    if top_p:
        request_data["top_p"] = top_p

    if top_k:
        request_data["top_k"] = top_k

    if is_verbose:
        print(f"[{quiz_id}] Request: {request_data}", file=sys.stderr)

    request_json = json.dumps(request_data)
    response_json = None

    request_file_path = os.path.join(output_dir, f"{quiz_id}_request.json") if output_dir else None
    response_file_path = os.path.join(output_dir, f"{quiz_id}_response.json") if output_dir else None

    if output_dir and os.path.exists(request_file_path) and os.path.exists(response_file_path):
        # Skip API call if model response is already saved in a JSON file
        if is_verbose:
            print(f"{quiz_id} Skipping already answered quiz", file=sys.stderr)

        with open(response_file_path, "r") as f:
            response_json = json.load(f)
    else:
        # Perform API call and store request/response in JSON files.

        for try_num in range(max_retries):
            try:
                response = requests.post(
                    url = api_url,
                    headers = { "Content-Type": "application/json", "Authorization": f"Bearer {api_key}" },
                    data=json.dumps(request_data),
                )

                if is_verbose:
                    print(f"[{quiz_id}] Response status code: {response.status_code}", file=sys.stderr)

                if is_verbose:
                    print(f"[{quiz_id}] Response: {response.text.strip()}", file=sys.stderr)

                if response.status_code != 200:
                    raise RuntimeError(f"Response status code: {response.status_code}")

                response_json = response.json()

                if "error" in response_json:
                    raise RuntimeError("Server error")

                if "error" in response_json["choices"][0]:
                    raise RuntimeError("Upstream server error")

                if request_file_path and response_file_path:
                    with open(request_file_path, "w") as f:
                        f.write(request_json)
                    with open(response_file_path, "w") as f:
                        f.write(response.text.strip())

                break
            except Exception as ex:
                print(f"[{quiz_id}] Caught exception: {ex}", file=sys.stderr)
                time.sleep(60)
                continue

    if not response_json:
        return None

    model_response = response_json["choices"][0]["message"]["content"]

    if "provider" in response_json:
        provider_name = response_json["provider"]
    else:
        provider_name = None

    return [problem_size, relation_name, correct_answer, quiz, model_name, provider_name, reasoning_effort, system_prompt, model_response]

results = process_map(make_request, list(quiz_reader), max_workers=num_threads)

for result in results:
    if result:
        csv_writer.writerow(result)

print(f"Successfully generated {sum(1 for result in results if result)} of {len(results)} quiz solutions.", file=sys.stderr)


#!/usr/bin/env -S python3 -u

import os
import csv
import sys
import argparse
import time
import json
import requests
from concurrent.futures import ThreadPoolExecutor

DEFAULT_SYSTEM_PROMPT="You are a master of logical thinking. You carefully analyze the premises step by step, take detailed notes and draw intermediate conclusions based on which you can find the final answer to any question."

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", help="OpenRouter model name.", required=True)
parser.add_argument("-p", "--provider", help="OpenRouter provider name.")
parser.add_argument("-e", "--effort", help="Reasoning effort (o1 model only).")
parser.add_argument("-t", "--threads", help="Number of threads to use.", type=int, default=8)
parser.add_argument("-v", "--verbose", help="Enable verbose output.", action="store_true")
parser.add_argument("-s", "--system-prompt", help="Use given system prompt. By default, the system prompt is not used. When this option is passed without a value, the default system prompt value is used: " + repr(DEFAULT_SYSTEM_PROMPT), const=DEFAULT_SYSTEM_PROMPT, default=None, nargs='?')
parser.add_argument("-T", "--temp", help="Temperature value to use.", type=float, default=0.01)
parser.add_argument("-n", "--max-tokens", help="Max number of tokens to generate.", type=float, default=16384)
args = parser.parse_args()
model_name = args.model
provider_name = args.provider
system_prompt = args.system_prompt
reasoning_effort = args.effort
num_threads = args.threads
is_verbose = args.verbose
temperature = args.temp
max_tokens = args.max_tokens

quiz_reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
csv_writer = csv.writer(sys.stdout)
api_key = os.getenv("OPENROUTER_API_KEY")

def make_request(row):
    global provider_name
    global system_prompt
    global reasoning_effort
    global api_key
    global is_verbose

    if is_verbose:
        print("Processing quiz", file=sys.stderr)

    problem_size, relation_name, correct_answer, quiz = row

    system_messages=[{"role": "system", "content": system_prompt }]
    messages=[{"role": "user", "content": quiz }]
    if system_prompt is not None:
        messages = system_messages + messages

    request_data = {
        "model": model_name,
        "temperature": temperature,
        "seed": 42,
        "max_tokens": max_tokens,
        "messages": messages,
    }

    if provider_name:
        request_data["provider"] = { "order": [ provider_name ], "allow_fallbacks": False }

    if reasoning_effort:
        assert(reasoning_effort in ["low", "medium", "high"])
        request_data["reasoning_effort"] = reasoning_effort

    if is_verbose:
        print(f"Request: {request_data}", file=sys.stderr)

    while True:
        try:
            response = requests.post(
                url = "https://openrouter.ai/api/v1/chat/completions",
                headers = { "Authorization": f"Bearer {api_key}" },
                data=json.dumps(request_data),
            )

            if is_verbose:
                print(f"Response status code: {response.status_code}", file=sys.stderr)

            if response.status_code != 200:
                time.sleep(60)
                continue

            response_json = response.json()

            if is_verbose:
                print(f"Response: {response_json}", file=sys.stderr)

            model_response = response_json["choices"][0]["message"]["content"]
            provider_name = response_json["provider"]
            break
        except Exception as ex:
            print(f"Caught exception: {ex}", file=sys.stderr)
            time.sleep(60)
            continue

    assert(response.status_code == 200)

    return [problem_size, relation_name, correct_answer, quiz, model_name, provider_name, reasoning_effort, system_prompt, model_response]

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    results = executor.map(make_request, quiz_reader)

for result in results:
    csv_writer.writerow(result)


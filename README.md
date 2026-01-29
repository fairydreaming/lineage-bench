# lineage-bench
Testing LLM reasoning abilities with lineage relationship quizzes. 

The project is a successor of the [farel-bench](https://github.com/fairydreaming/farel-bench) benchmark.

## Changelog

* 2026-01-28 - Added `--api` and `--verbosity` options in `run_openrouter.py`. Temperature is now an optional parameter without a default value. Caching of model responses is now optional.
* 2026-01-24 - Exctracted benchmark results to separate [lineage-bench-results](https://github.com/fairydreaming/lineage-bench-results) repository.
* 2025-12-18 - Added xhigh reasoning effort in `run_openrouter.py`.
* 2025-11-20 - Added progress monitoring with tqdm and caching of model responses in `--output` directory in `run_openrouter.py`.
* 2025-11-18 - Added `--effort`, `--top-p` and `--top-k` options in `run_openrouter.py`.

## Results

Benchmark results are now in a separate [lineage-bench-results](https://github.com/fairydreaming/lineage-bench-results) repository.

Most recent results are in the [lineage-8_64_128_192](https://github.com/fairydreaming/lineage-bench-results/tree/main/lineage-8_64_128_192) directory.

## Description
The purpose of this project is to test LLM reasoning abilities with lineage relationship quizzes.

The general idea is to make LLM reason about a graph of lineage relationships where nodes are people and edges are ancestor/descendant relations between people.
LLM is asked to determine the lineage relationship between two people A and B based on the graph.
By varying the number of graph nodes (problem size) we can control the quiz difficulty.

There are five possible answers in each quiz:
1. A is B's ancestor
2. A is B's descendant
3. A and B share a common ancestor
4. A and B share a common descendant
5. None of the above is correct.

The last answer is never correct. It serves only as an invalid fallback answer.

## Examples
Below you can see some example lineage relationship graphs and corresponding quizzes.

![lineage-bench.png](https://i.postimg.cc/Px7VSZRL/lineage-bench.png)

### Ancestor
```
Given the following lineage relationships:
* Joseph is George's ancestor.
* Henry is George's descendant.
* Thomas is Joseph's ancestor.
Determine the lineage relationship between Thomas and Henry.
Select the correct answer:
1. Thomas is Henry's ancestor.
2. Thomas is Henry's descendant.
3. Thomas and Henry share a common ancestor.
4. Thomas and Henry share a common descendant.
5. None of the above is correct.
Enclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>.
```

### Common ancestor
```
Given the following lineage relationships:
* Matthew is Heather's ancestor.
* Heather is Melissa's ancestor.
* Matthew is Mark's ancestor.
Determine the lineage relationship between Mark and Melissa.
Select the correct answer:
1. Mark and Melissa share a common ancestor.
2. Mark is Melissa's ancestor.
3. Mark and Melissa share a common descendant.
4. Mark is Melissa's descendant.
5. None of the above is correct.
Enclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>.
```

### Common descendant
```
Given the following lineage relationships:
* Madison is Kathleen's descendant.
* Judith is Madison's ancestor.
* Harold is Kathleen's ancestor.
Determine the lineage relationship between Harold and Judith.
Select the correct answer:
1. Harold and Judith share a common descendant.
2. Harold and Judith share a common ancestor.
3. Harold is Judith's ancestor.
4. Harold is Judith's descendant.
5. None of the above is correct.
Enclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>.
```

## Usage

The usual workflow is to:

1. Run lineage_bench.py to generate lineage relationship quizzes.
2. Run run_openrouter.py to test LLM models.
3. Run compute_metrics.py to calculate benchmark results.
4. Run plot_stacked.py to generate a results plot.

Output is usually written to the standard output. Input is usually read from the standard input.

Example usage:
```
$ ./lineage_bench.py -s -l 8 -n 10 -r 42|./run_openrouter.py -m "google/gemini-pro-1.5" -t 8 -r -o results/gemini-pro-1.5 -v|tee results/gemini-pro-1.5_8.csv
$ cat results/*.csv|./compute_metrics.py --csv --relaxed|./plot_stacked.py -o results.png
```

I usually run the benchmark like this:

```
for length in 8 16 32 64
do
  ./lineage_bench.py -s -l $length -n 50 -r 42|./run_openrouter.py -m <model> -p <provider> -o <cache_dir> -r -v|tee results/<model>_$length.csv
done
```

This results in 200 generated quizzes per problem size, 800 quizzes overall in a single benchmark run.

### lineage_bench.py

```
usage: lineage_bench.py [-h] -l [4-200] [-p PROMPT] [-s] [-n NUMBER] [-r SEED]

options:
  -h, --help            show this help message and exit
  -l [4-200], --length [4-200]
                        Number of people connected with lineage relationships in the quiz.
  -p PROMPT, --prompt PROMPT
                        Prompt template of the quiz. The default prompt template is: 'Given the following lineage
                        relationships:\n{quiz_relations}\n{quiz_question}\nSelect the correct
                        answer:\n{quiz_answers}\nEnclose the selected answer number in the <ANSWER> tag, for example:
                        <ANSWER>1</ANSWER>.'
  -s, --shuffle         Shuffle the order of lineage relations in the quiz.
  -n NUMBER, --number NUMBER
                        Number of quizzes generated for each valid answer option.
  -r SEED, --seed SEED  Random seed value
```

### run_openrouter.py

Before running `run_openrouter.py` set OPENROUTER_API_KEY environment variable to your OpenRouter, OpenAI or ZenMux API Key.

```
usage: run_openrouter.py [-h] [-a {openrouter,openai,zenmux}] [-u URL] -m MODEL [-o OUTPUT] [-p PROVIDER] [-r]
                         [-e {low,medium,high,xhigh}] [-t THREADS] [-v] [-s [SYSTEM_PROMPT]] [-T TEMP] [-P TOP_P]
                         [-K TOP_K] [-n MAX_TOKENS] [-V {low,medium,high}] [-i RETRIES]

options:
  -h, --help            show this help message and exit
  -a {openrouter,openai,zenmux}, --api {openrouter,openai,zenmux}
                        API Provider
  -u URL, --url URL     OpenAI-compatible API URL
  -m MODEL, --model MODEL
                        OpenRouter model name.
  -o OUTPUT, --output OUTPUT
                        Directory for storing model responses.
  -p PROVIDER, --provider PROVIDER
                        OpenRouter provider name.
  -r, --reasoning       Enable reasoning.
  -e {low,medium,high,xhigh}, --effort {low,medium,high,xhigh}
                        Reasoning effort (recent OpenAI and xAI models support this).
  -t THREADS, --threads THREADS
                        Number of threads to use.
  -v, --verbose         Enable verbose output.
  -s [SYSTEM_PROMPT], --system-prompt [SYSTEM_PROMPT]
                        Use given system prompt. By default, the system prompt is not used. When this option is passed
                        without a value, the default system prompt value is used: 'You are a master of logical thinking.
                        You carefully analyze the premises step by step, take detailed notes and draw intermediate
                        conclusions based on which you can find the final answer to any question.'
  -T TEMP, --temp TEMP  Temperature value to use.
  -P TOP_P, --top-p TOP_P
                        top_p sampling parameter.
  -K TOP_K, --top-k TOP_K
                        top_k sampling parameter.
  -n MAX_TOKENS, --max-tokens MAX_TOKENS
                        Max number of tokens to generate.
  -V {low,medium,high}, --verbosity {low,medium,high}
                        Model verbosity (recent OpenAI models support this).
  -i RETRIES, --retries RETRIES
                        Max number of API request retries.
```

### compute_metrics.py

```
usage: compute_metrics.py [-h] [-c] [-r] [-d]

options:
  -h, --help      show this help message and exit
  -c, --csv       Generate CSV output.
  -r, --relaxed   Relaxed answer format requirements
  -d, --detailed  Generate detailed output
```

### plot_line.py

```
usage: plot_line.py [-h] [-o OUTPUT] [-n TOP_N]

options:
  -h, --help           show this help message and exit
  -o, --output OUTPUT  Write rendered plot to this file.
  -n, --top-n TOP_N    Show only n best results.
```

### plot_stacked.py

```
usage: plot_stacked.py [-h] [-o OUTPUT] [-n TOP_N]

options:
  -h, --help           show this help message and exit
  -o, --output OUTPUT  Write rendered plot to this file.
  -n, --top-n TOP_N    Show only n best results.
```

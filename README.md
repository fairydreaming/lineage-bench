# lineage-bench
Testing LLM reasoning abilities with lineage relationship quizzes. 

The project is a successor of the [farel-bench](https://github.com/fairydreaming/farel-bench) benchmark.

**Note: This benchmark seems to be already saturated by Claude Sonnet 4.5 and recently released Gemini 3 Pro Preview even for 192 problem size. I'm very happy with this progress!**

## Changelog

* 2025-11-25 - Added results for gpt-5.1, claude-opus-4.5, grok-4.1-fast and o4-mini.
* 2025-11-23 - Added results for qwen3-32b, o3-mini and o3 models.
* 2025-11-22 - Updated results to include recently released models, but only with 40 quizzes per problem size to reduce costs. Extended range of problem lengths to increase difficulty. Added file-based caching of model requests and responses.
* 2025-03-07 - Added results for qwq-32b (used Parasail provider with 0.01 temp, observed some infinite loop generations, but mostly for lineage-64 where the model performs bad anyway).
* 2025-03-04 - Updated results for perplexity/r1-1776. (apparently there was a problem with the model serving stack, that's why r1-1776 initially performed worse than expected)
* 2025-02-26 - Added results for claude-3.7-sonnet (also with :thinking) and r1-1776
* 2025-02-20 - Updated results for deepseek/deepseek-r1-distill-llama-70b. (used Groq provider with 0.5 temperature)
* 2025-02-18 - Added results for kimi-k1.5-preview and llama-3.1-tulu-3-405b.
* 2025-02-06 - Added results for o1, o3-mini, qwen-max, gemini-exp-1206, deepseek-r1-distill-qwen-14b and deepseek-r1-distill-qwen-32b.
* 2025-01-24 - Added results for deepseek-r1-distill-llama-70b.
* 2025-01-20 - Added results for deepseek-r1.
* 2025-01-15 - Added results for deepseek-v3, gemini-2.0-flash-exp, gemini-2.0-flash-thinking-exp-1219 and minimax-01.

## Results

### Plot

#### Current results

![results_stacked](https://github.com/user-attachments/assets/5d54b85d-1daf-4f7d-9771-e75fc9621398)

#### Old results

![results_stacked](https://github.com/user-attachments/assets/559e686c-ce1e-4c9d-851e-1d9e2eb6f6b1)

### Table

The table below presents the benchmark results. Medium reasoning effort was used in Claude Opus 4.5, OpenAI and xAI models.

|   Nr | model_name                             |   lineage |   lineage-8 |   lineage-64 |   lineage-128 |   lineage-192 |
|-----:|:---------------------------------------|----------:|------------:|-------------:|--------------:|--------------:|
|    1 | google/gemini-3-pro-preview            |     0.969 |       1.000 |        1.000 |         0.925 |         0.950 |
|    2 | anthropic/claude-sonnet-4.5            |     0.944 |       0.975 |        0.975 |         0.900 |         0.925 |
|    3 | openai/gpt-5.1                         |     0.888 |       1.000 |        0.950 |         0.875 |         0.725 |
|    4 | qwen/qwen3-max                         |     0.869 |       1.000 |        0.800 |         0.900 |         0.775 |
|    5 | anthropic/claude-opus-4.5              |     0.869 |       1.000 |        0.950 |         0.900 |         0.625 |
|    5 | x-ai/grok-4                            |     0.869 |       1.000 |        0.950 |         0.900 |         0.625 |
|    5 | x-ai/grok-4-fast                       |     0.869 |       1.000 |        0.925 |         0.900 |         0.650 |
|    8 | qwen/qwen3-235b-a22b-thinking-2507     |     0.856 |       0.900 |        0.875 |         0.850 |         0.800 |
|    9 | deepseek/deepseek-v3.1-terminus:exacto |     0.812 |       0.975 |        0.900 |         0.700 |         0.675 |
|   10 | openai/o3                              |     0.800 |       1.000 |        0.925 |         0.800 |         0.475 |
|   11 | deepseek/deepseek-v3.2-exp             |     0.794 |       0.975 |        0.900 |         0.700 |         0.600 |
|   12 | anthropic/claude-haiku-4.5             |     0.794 |       0.975 |        0.925 |         0.575 |         0.700 |
|   13 | openai/gpt-5                           |     0.788 |       1.000 |        0.975 |         0.850 |         0.325 |
|   14 | deepcogito/cogito-v2.1-671b            |     0.756 |       0.975 |        0.800 |         0.650 |         0.600 |
|   15 | x-ai/grok-4.1-fast                     |     0.750 |       1.000 |        0.900 |         0.800 |         0.300 |
|   16 | qwen/qwen3-next-80b-a3b-thinking       |     0.575 |       0.950 |        0.700 |         0.425 |         0.225 |
|   17 | openai/gpt-oss-120b:exacto             |     0.544 |       1.000 |        0.825 |         0.325 |         0.025 |
|   18 | minimax/minimax-m2                     |     0.531 |       1.000 |        0.575 |         0.350 |         0.200 |
|   19 | moonshotai/kimi-k2-thinking            |     0.525 |       1.000 |        0.850 |         0.200 |         0.050 |
|   19 | openai/o4-mini                         |     0.525 |       1.000 |        0.775 |         0.300 |         0.025 |
|   21 | openai/gpt-5-mini                      |     0.512 |       1.000 |        0.950 |         0.075 |         0.025 |
|   22 | z-ai/glm-4.6:exacto                    |     0.506 |       0.925 |        0.600 |         0.350 |         0.150 |
|   23 | qwen/qwen3-30b-a3b-thinking-2507       |     0.494 |       1.000 |        0.575 |         0.275 |         0.125 |
|   24 | allenai/olmo-3-32b-think               |     0.444 |       0.925 |        0.600 |         0.175 |         0.075 |
|   25 | qwen/qwen3-32b                         |     0.362 |       0.950 |        0.475 |         0.025 |         0.000 |
|   26 | openai/gpt-5-nano                      |     0.294 |       1.000 |        0.150 |         0.025 |         0.000 |
|   27 | openai/o3-mini                         |     0.287 |       0.950 |        0.200 |         0.000 |         0.000 |

Each row contains the average benchmark score across all problem sizes, and separate scores for each problem size.

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
usage: lineage_bench.py [-h] -l LENGTH [-p PROMPT] [-s] [-n NUMBER] [-r SEED]

options:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Number of people connected with lineage relationships in the quiz.
  -p PROMPT, --prompt PROMPT
                        Prompt template of the quiz. The default prompt template is: 'Given the following lineage
                        relationships:\n{quiz_relations}\n{quiz_question}\nSelect the correct answer:\n{quiz_answers}\nEnclose the selected
                        answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>.'
  -s, --shuffle         Shuffle the order of lineage relations in the quiz.
  -n NUMBER, --number NUMBER
                        Number of quizzes generated for each valid answer option.
  -r SEED, --seed SEED  Random seed value
```

### run_openrouter.py

Before running `run_openrouter.py` set OPENROUTER_API_KEY environment variable to your OpenRouter API Key.

```
usage: run_openrouter.py [-h] [-u URL] -m MODEL -o OUTPUT [-p PROVIDER] [-r] [-e EFFORT] [-t THREADS] [-v] [-s [SYSTEM_PROMPT]] [-T TEMP]
                         [-P TOP_P] [-K TOP_K] [-n MAX_TOKENS] [-i RETRIES]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     OpenAI-compatible API URL
  -m MODEL, --model MODEL
                        OpenRouter model name.
  -o OUTPUT, --output OUTPUT
                        Directory for storing model responses.
  -p PROVIDER, --provider PROVIDER
                        OpenRouter provider name.
  -r, --reasoning       Enable reasoning.
  -e EFFORT, --effort EFFORT
                        Reasoning effort (recent OpenAI and xAI models support this).
  -t THREADS, --threads THREADS
                        Number of threads to use.
  -v, --verbose         Enable verbose output.
  -s [SYSTEM_PROMPT], --system-prompt [SYSTEM_PROMPT]
                        Use given system prompt. By default, the system prompt is not used. When this option is passed without a value, the
                        default system prompt value is used: 'You are a master of logical thinking. You carefully analyze the premises step by
                        step, take detailed notes and draw intermediate conclusions based on which you can find the final answer to any
                        question.'
  -T TEMP, --temp TEMP  Temperature value to use.
  -P TOP_P, --top-p TOP_P
                        top_p sampling parameter.
  -K TOP_K, --top-k TOP_K
                        top_k sampling parameter.
  -n MAX_TOKENS, --max-tokens MAX_TOKENS
                        Max number of tokens to generate.
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
usage: plot_line.py [-h] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Write rendered plot to this file.
```

### plot_stacked.py

```
usage: plot_stacked.py [-h] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Write rendered plot to this file.
```

# lineage-bench
Testing LLM reasoning abilities with lineage relationship quizzes. 

The project is a successor of the [farel-bench](https://github.com/fairydreaming/farel-bench) benchmark.

## Changelog

* 2024-03-07 - Added results for qwq-32b (used Parasail provider with 0.01 temp, observed some infinite loop generations, but mostly for lineage-64 where the model performs bad anyway).
* 2024-03-04 - Updated results for perplexity/r1-1776. (apparently there was a problem with the model serving stack, that's why r1-1776 initially performed worse than expected)
* 2024-02-26 - Added results for claude-3.7-sonnet (also with :thinking) and r1-1776
* 2024-02-20 - Updated results for deepseek/deepseek-r1-distill-llama-70b. (used Groq provider with 0.5 temperature)
* 2024-02-18 - Added results for kimi-k1.5-preview and llama-3.1-tulu-3-405b.
* 2024-02-06 - Added results for o1, o3-mini, qwen-max, gemini-exp-1206, deepseek-r1-distill-qwen-14b and deepseek-r1-distill-qwen-32b.
* 2024-01-24 - Added results for deepseek-r1-distill-llama-70b.
* 2024-01-20 - Added results for deepseek-r1.
* 2024-01-15 - Added results for deepseek-v3, gemini-2.0-flash-exp, gemini-2.0-flash-thinking-exp-1219 and minimax-01.

## Results

### Plot

![results_stacked](https://github.com/user-attachments/assets/001fc02a-6d06-4a2c-a1c5-1797c753473b)

### Table

The table below presents the benchmark results.

|   Nr | model_name                             |   lineage |   lineage-8 |   lineage-16 |   lineage-32 |   lineage-64 |
|-----:|:---------------------------------------|----------:|------------:|-------------:|-------------:|-------------:|
|    1 | perplexity/r1-1776                     |     0.934 |       0.965 |        0.985 |        0.935 |        0.850 |
|    2 | openai/o1                              |     0.921 |       1.000 |        0.980 |        0.925 |        0.780 |
|    3 | deepseek/deepseek-r1                   |     0.917 |       0.965 |        0.980 |        0.945 |        0.780 |
|    4 | anthropic/claude-3.7-sonnet:thinking   |     0.898 |       0.985 |        0.970 |        0.910 |        0.725 |
|    5 | deepseek/deepseek-r1-distill-llama-70b |     0.734 |       0.925 |        0.830 |        0.660 |        0.520 |
|    6 | openai/o3-mini                         |     0.726 |       0.970 |        0.945 |        0.795 |        0.195 |
|    7 | qwen/qwq-32b                           |     0.695 |       0.960 |        0.915 |        0.690 |        0.215 |
|    8 | kimi-k1.5-preview                      |     0.613 |       0.830 |        0.655 |        0.635 |        0.330 |
|    8 | deepseek/deepseek-r1-distill-qwen-32b  |     0.613 |       0.805 |        0.685 |        0.595 |        0.365 |
|   10 | deepseek/deepseek-chat                 |     0.610 |       0.860 |        0.590 |        0.530 |        0.460 |
|   11 | openai/o1-mini                         |     0.562 |       0.955 |        0.820 |        0.400 |        0.075 |
|   12 | gemini-exp-1206                        |     0.517 |       0.640 |        0.495 |        0.455 |        0.480 |
|   13 | google/gemini-pro-1.5                  |     0.492 |       0.620 |        0.530 |        0.440 |        0.380 |
|   14 | openai/gpt-4o-2024-11-20               |     0.490 |       0.755 |        0.545 |        0.425 |        0.235 |
|   15 | meta-llama/llama-3.1-405b-instruct     |     0.489 |       0.660 |        0.590 |        0.465 |        0.240 |
|   16 | qwen/qwq-32b-preview                   |     0.476 |       0.845 |        0.585 |        0.315 |        0.160 |
|   17 | mistralai/mistral-large-2411           |     0.475 |       0.695 |        0.510 |        0.360 |        0.335 |
|   17 | allenai/llama-3.1-tulu-3-405b          |     0.475 |       0.710 |        0.505 |        0.335 |        0.350 |
|   19 | qwen/qwen-max                          |     0.463 |       0.710 |        0.435 |        0.410 |        0.295 |
|   20 | meta-llama/llama-3.3-70b-instruct      |     0.438 |       0.625 |        0.485 |        0.340 |        0.300 |
|   21 | deepseek/deepseek-r1-distill-qwen-14b  |     0.428 |       0.830 |        0.600 |        0.200 |        0.080 |
|   22 | x-ai/grok-2-1212                       |     0.405 |       0.580 |        0.395 |        0.360 |        0.285 |
|   23 | gemini-2.0-flash-thinking-exp-1219     |     0.395 |       0.595 |        0.465 |        0.325 |        0.195 |
|   24 | anthropic/claude-3.7-sonnet            |     0.359 |       0.790 |        0.440 |        0.155 |        0.050 |
|   25 | minimax/minimax-01                     |     0.292 |       0.560 |        0.370 |        0.155 |        0.085 |
|   26 | gemini-2.0-flash-exp                   |     0.247 |       0.460 |        0.190 |        0.200 |        0.140 |
|   27 | anthropic/claude-3.5-sonnet            |     0.221 |       0.645 |        0.205 |        0.035 |        0.000 |

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
$ ./lineage_bench.py -s -l 8 -n 10 -r 42|./run_openrouter.py -m "google/gemini-pro-1.5" -t 8 -v|tee results/gemini-pro-1.5_8.csv
$ cat results/*.csv|./compute_metrics.py --csv --relaxed|./plot_stacked.py -o results.png
```

I usually run the benchmark like this:

```
for length in 8 16 32 64
do
  ./lineage_bench.py -s -l $length -n 50 -r 42|./run_openrouter.py -m <model> -p <provider> -v|tee results/<model>_$length.log
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

```
usage: run_openrouter.py [-h] -m MODEL [-p PROVIDER] [-e EFFORT] [-t THREADS] [-v] [-s [SYSTEM_PROMPT]]

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        OpenRouter model name.
  -p PROVIDER, --provider PROVIDER
                        OpenRouter provider name.
  -e EFFORT, --effort EFFORT
                        Reasoning effort (o1 model only).
  -t THREADS, --threads THREADS
                        Number of threads to use.
  -v, --verbose         Enable verbose output.
  -s [SYSTEM_PROMPT], --system-prompt [SYSTEM_PROMPT]
                        Use given system prompt. By default, the system prompt is not used. When this option is passed without a value, the
                        default system prompt value is used: 'You are a master of logical thinking. You carefully analyze the premises step by
                        step, take detailed notes and draw intermediate conclusions based on which you can find the final answer to any
                        question.'
  -T TEMP, --temp TEMP  Temperature value to use.
  -n MAX_TOKENS, --max-tokens MAX_TOKENS
                        Max number of tokens to generate.
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

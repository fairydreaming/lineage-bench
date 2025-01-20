# lineage-bench
Testing LLM reasoning abilities with lineage relationship quizzes. 

The project is a successor of the [farel-bench](https://github.com/fairydreaming/farel-bench) benchmark.

## Results

### Plot

![results](https://github.com/user-attachments/assets/cf469106-cc1e-4da3-81e5-62fad9e94ee7)

### Table

The table below presents the benchmark results.

|   Nr | model_name                         |   lineage |   lineage-8 |   lineage-16 |   lineage-32 |   lineage-64 |
|-----:|:-----------------------------------|----------:|------------:|-------------:|-------------:|-------------:|
|    1 | deepseek/deepseek-r1               |      0.92 |        0.96 |         0.98 |         0.94 |         0.78 |
|    2 | deepseek/deepseek-chat             |      0.61 |        0.86 |         0.59 |         0.53 |         0.46 |
|    3 | openai/o1-mini                     |      0.56 |        0.95 |         0.82 |         0.40 |         0.08 |
|    4 | google/gemini-pro-1.5              |      0.49 |        0.62 |         0.53 |         0.44 |         0.38 |
|    5 | openai/gpt-4o-2024-11-20           |      0.49 |        0.76 |         0.55 |         0.42 |         0.23 |
|    6 | meta-llama/llama-3.1-405b-instruct |      0.49 |        0.66 |         0.59 |         0.46 |         0.24 |
|    7 | qwen/qwq-32b-preview               |      0.48 |        0.85 |         0.59 |         0.32 |         0.16 |
|    8 | mistralai/mistral-large-2411       |      0.47 |        0.69 |         0.51 |         0.36 |         0.34 |
|    9 | meta-llama/llama-3.3-70b-instruct  |      0.44 |        0.62 |         0.48 |         0.34 |         0.30 |
|   10 | x-ai/grok-2-1212                   |      0.41 |        0.58 |         0.40 |         0.36 |         0.29 |
|   11 | gemini-2.0-flash-thinking-exp-1219 |      0.40 |        0.59 |         0.46 |         0.33 |         0.20 |
|   12 | minimax/minimax-01                 |      0.29 |        0.56 |         0.37 |         0.15 |         0.09 |
|   13 | gemini-2.0-flash-exp               |      0.25 |        0.46 |         0.19 |         0.20 |         0.14 |
|   14 | anthropic/claude-3.5-sonnet        |      0.22 |        0.65 |         0.21 |         0.04 |         0.00 |

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
4. Run plot_graph.py to generate a results plot.

Output is usually written to the standard output. Input is usually read from the standard input.

Example usage:
```
$ ./lineage_bench.py -s -l 8 -n 10 -r 42|./run_openrouter.py -m "google/gemini-pro-1.5" -t 8 -v|tee results/gemini-pro-1.5_8.csv
$ cat results/*.csv|./compute_metrics.py --csv|./plot_graph.py -o results.png
```

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
```

### compute_metrics.py

```
usage: compute_metrics.py [-h] [-c]

options:
  -h, --help  show this help message and exit
  -c, --csv   Generate CSV output.
```

### plot_graph.py

```
usage: plot_graph.py [-h] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Write rendered plot to this file.
```

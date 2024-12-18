# lineage-bench
Testing LLM reasoning abilities with lineage relationship quizzes. 

The project is a successor of the [farel-bench](https://github.com/fairydreaming/farel-bench) benchmark.

## Results

### Plot

![Lineage Benchmark Results Plot](https://i.postimg.cc/8z7wssKw/results.png)

### Problem size 8

|   Nr |   problem size | model name                         |   lineage |   ANCESTOR |   DESCENDANT |   COMMON ANCESTOR |   COMMON DESCENDANT |
|-----:|---------------:|:-----------------------------------|----------:|-----------:|-------------:|------------------:|--------------------:|
|    1 |              8 | openai/o1-mini                     |      0.95 |       0.98 |         0.88 |              1.00 |                0.96 |
|    2 |              8 | qwen/qwq-32b-preview               |      0.85 |       0.86 |         0.92 |              0.96 |                0.64 |
|    3 |              8 | openai/gpt-4o-2024-11-20           |      0.76 |       0.92 |         0.74 |              0.94 |                0.42 |
|    4 |              8 | mistralai/mistral-large-2411       |      0.69 |       0.92 |         0.82 |              0.70 |                0.34 |
|    5 |              8 | meta-llama/llama-3.1-405b-instruct |      0.66 |       0.74 |         0.58 |              0.80 |                0.52 |
|    6 |              8 | anthropic/claude-3.5-sonnet        |      0.65 |       0.60 |         0.52 |              0.78 |                0.68 |
|    7 |              8 | meta-llama/llama-3.3-70b-instruct  |      0.62 |       0.58 |         0.62 |              0.92 |                0.38 |
|    8 |              8 | google/gemini-pro-1.5              |      0.62 |       0.74 |         0.42 |              0.94 |                0.38 |
|    9 |              8 | x-ai/grok-2-1212                   |      0.58 |       0.80 |         0.60 |              0.60 |                0.32 |

### Problem size 16

|   Nr |   problem size | model name                         |   lineage |   ANCESTOR |   DESCENDANT |   COMMON ANCESTOR |   COMMON DESCENDANT |
|-----:|---------------:|:-----------------------------------|----------:|-----------:|-------------:|------------------:|--------------------:|
|    1 |             16 | openai/o1-mini                     |      0.82 |       0.84 |         0.80 |              0.90 |                0.74 |
|    2 |             16 | meta-llama/llama-3.1-405b-instruct |      0.59 |       0.74 |         0.50 |              0.82 |                0.30 |
|    3 |             16 | qwen/qwq-32b-preview               |      0.59 |       0.60 |         0.52 |              0.64 |                0.58 |
|    4 |             16 | openai/gpt-4o-2024-11-20           |      0.55 |       0.78 |         0.54 |              0.68 |                0.18 |
|    5 |             16 | google/gemini-pro-1.5              |      0.53 |       0.60 |         0.42 |              0.90 |                0.20 |
|    6 |             16 | mistralai/mistral-large-2411       |      0.51 |       0.88 |         0.58 |              0.52 |                0.06 |
|    7 |             16 | meta-llama/llama-3.3-70b-instruct  |      0.48 |       0.58 |         0.28 |              0.98 |                0.10 |
|    8 |             16 | x-ai/grok-2-1212                   |      0.40 |       0.52 |         0.24 |              0.56 |                0.26 |
|    9 |             16 | anthropic/claude-3.5-sonnet        |      0.21 |       0.10 |         0.04 |              0.28 |                0.40 |

### Problem size 32

|   Nr |   problem size | model name                         |   lineage |   ANCESTOR |   DESCENDANT |   COMMON ANCESTOR |   COMMON DESCENDANT |
|-----:|---------------:|:-----------------------------------|----------:|-----------:|-------------:|------------------:|--------------------:|
|    1 |             32 | meta-llama/llama-3.1-405b-instruct |      0.46 |       0.62 |         0.30 |              0.78 |                0.16 |
|    2 |             32 | google/gemini-pro-1.5              |      0.44 |       0.56 |         0.44 |              0.56 |                0.20 |
|    3 |             32 | openai/gpt-4o-2024-11-20           |      0.42 |       0.66 |         0.34 |              0.52 |                0.18 |
|    4 |             32 | openai/o1-mini                     |      0.40 |       0.42 |         0.38 |              0.46 |                0.34 |
|    5 |             32 | x-ai/grok-2-1212                   |      0.36 |       0.40 |         0.26 |              0.54 |                0.24 |
|    6 |             32 | mistralai/mistral-large-2411       |      0.36 |       0.58 |         0.26 |              0.56 |                0.04 |
|    7 |             32 | meta-llama/llama-3.3-70b-instruct  |      0.34 |       0.36 |         0.06 |              0.92 |                0.02 |
|    8 |             32 | qwen/qwq-32b-preview               |      0.32 |       0.32 |         0.20 |              0.44 |                0.30 |
|    9 |             32 | anthropic/claude-3.5-sonnet        |      0.04 |       0.04 |         0.00 |              0.02 |                0.08 |

### Problem size 64

|   Nr |   problem size | model name                         |   lineage |   ANCESTOR |   DESCENDANT |   COMMON ANCESTOR |   COMMON DESCENDANT |
|-----:|---------------:|:-----------------------------------|----------:|-----------:|-------------:|------------------:|--------------------:|
|    1 |             64 | google/gemini-pro-1.5              |      0.38 |       0.58 |         0.28 |              0.50 |                0.16 |
|    2 |             64 | mistralai/mistral-large-2411       |      0.34 |       0.42 |         0.22 |              0.62 |                0.08 |
|    3 |             64 | meta-llama/llama-3.3-70b-instruct  |      0.30 |       0.26 |         0.04 |              0.90 |                0.00 |
|    4 |             64 | x-ai/grok-2-1212                   |      0.29 |       0.38 |         0.24 |              0.44 |                0.08 |
|    5 |             64 | meta-llama/llama-3.1-405b-instruct |      0.24 |       0.24 |         0.18 |              0.50 |                0.04 |
|    6 |             64 | openai/gpt-4o-2024-11-20           |      0.23 |       0.36 |         0.12 |              0.36 |                0.10 |
|    7 |             64 | qwen/qwq-32b-preview               |      0.16 |       0.14 |         0.02 |              0.30 |                0.18 |
|    8 |             64 | openai/o1-mini                     |      0.08 |       0.10 |         0.02 |              0.08 |                0.10 |
|    9 |             64 | anthropic/claude-3.5-sonnet        |      0.00 |       0.00 |         0.00 |              0.00 |                0.00 |


## Description
The purpose of this project is to test LLM reasoning abilities with lineage relationship quizzes.

The general idea is to make LLM reason about a graph of lineage relationships where nodes are people and edges are ancestor/descendant relations between people.
LLM is asked to determine the lineage relationship between two people A and B based on the graph.
By varying the number of graph nodes we can control the quiz difficulty.

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

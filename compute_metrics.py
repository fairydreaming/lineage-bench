#!/usr/bin/env python3

import os
import re
import sys
import pandas as pd
import argparse
from collections import defaultdict
import csv

def extract_answer(row):
    if type(row['model_response']) is not str:
        return 0

    matches = re.findall(r'<ANSWER>([0-9]*?)</ANSWER>', row['model_response'])
    if matches:
        return int(matches[0])
    else:
        matches = re.findall(r'boxed\{([0-9]*?)\}', row['model_response'])
        if matches:
            return int(matches[0])

    return 0

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--csv", help="Generate CSV output.", action="store_true")
args = parser.parse_args()

gen_csv = args.csv

df = pd.read_csv(sys.stdin, names=['problem_size', 'relation_name', 'correct_answer', 'quiz', 'model_name', 'provider_name', 'reasoning_effort', 'system_prompt', 'model_response'], dtype={'problem_size': 'int32', 'relation_name': 'object', 'correct_answer': 'int32', 'quiz': 'object', 'model_name': 'object', 'provider_name': 'object', 'reasoning_effort': 'object', 'system_prompt': 'object', 'model_response': 'object'})

df['model_answer'] = df.apply(extract_answer, axis=1)
df['answer_correct'] = df['correct_answer'] == df['model_answer']

df = df[['problem_size', 'relation_name', 'model_name', 'answer_correct']]

df = df.groupby(['problem_size', 'relation_name', 'model_name'])['answer_correct'].mean().reset_index().rename(columns={'answer_correct': 'percent_correct'})

df = df.pivot(index=['problem_size', 'model_name'], columns='relation_name', values='percent_correct').reset_index()

df['lineage'] = df[['ANCESTOR', 'DESCENDANT', 'COMMON_ANCESTOR', 'COMMON_DESCENDANT']].mean(axis=1)

df = df.sort_values(['lineage'], ascending=False)

df['Nr'] = df['lineage'].rank(method='min', ascending=False).astype('int32')

df = df[['Nr', 'problem_size', 'model_name', 'lineage', 'ANCESTOR', 'DESCENDANT', 'COMMON_ANCESTOR', 'COMMON_DESCENDANT']]

if gen_csv:
    print(df.to_csv(index=False))
else:
    print(df.to_markdown(floatfmt=".2f", index=False))



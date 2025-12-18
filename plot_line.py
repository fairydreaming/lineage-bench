#!/usr/bin/env python3

import sys
import argparse
import matplotlib.ticker as tck
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Write rendered plot to this file.")
parser.add_argument("-n", "--top-n", help="Show only n best results.", type=int, default=30)
args = parser.parse_args()

output_file = args.output
top_n = args.top_n

df = pd.read_csv(sys.stdin)

# get only top n results
df = df[:top_n]

col_names = df.columns[3:].values
problem_sizes = list(map(lambda c: int(c.removeprefix('lineage-')), col_names))

# Plot the data
plt.figure(figsize=(12, 8))

colormap = plt.cm.nipy_spectral
colors = colormap(np.linspace(0, 1, len(df['model_name'])))
plt.gca().set_prop_cycle('color', colors)

for index, row in df.iterrows():
    plt.plot(problem_sizes, row[col_names], marker='o', label=row['model_name'])

# Customize the plot
plt.title('Lineage benchmark scores for different problem sizes.')
plt.xlabel('Problem Size')
plt.ylabel('Lineage Score')
plt.legend(title='Model Name', loc='lower left')
plt.xscale('log')
plt.gca().get_xaxis().set_minor_locator(tck.AutoMinorLocator())
plt.xticks(problem_sizes)
plt.gca().get_xaxis().set_major_formatter(tck.ScalarFormatter())
plt.grid(True)
plt.tight_layout()

if output_file:
    plt.savefig(output_file)

# Show the plot
plt.show()


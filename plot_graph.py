#!/usr/bin/env python3

import sys
import argparse
import matplotlib.ticker as tck
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Write rendered plot to this file.")
args = parser.parse_args()

output_file = args.output

df = pd.read_csv(sys.stdin)

# Sort the DataFrame by model name and problem size for consistent plotting
df = df.sort_values(by=['model_name', 'problem_size'])

# Plot the data
plt.figure(figsize=(10, 6))

# Group by model name and plot each group
for model_name, group in df.groupby('model_name'):
    plt.plot(group['problem_size'], group['lineage'], marker='o', label=model_name)

# Customize the plot
plt.title('Lineage benchmark scores for different problem sizes.')
plt.xlabel('Problem Size')
plt.ylabel('Lineage Score')
plt.legend(title='Model Name', loc='upper right')
plt.xscale('log')
plt.gca().get_xaxis().set_minor_locator(tck.AutoMinorLocator())
plt.xticks([8, 16, 32, 64])
plt.gca().get_xaxis().set_major_formatter(tck.ScalarFormatter())
plt.grid(True)
plt.tight_layout()

if output_file:
    plt.savefig(output_file)

# Show the plot
plt.show()


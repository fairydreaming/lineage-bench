#!/usr/bin/env python3

import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Write rendered plot to this file.")
args = parser.parse_args()

output_file = args.output

# Read CSV data from stdin
df = pd.read_csv(sys.stdin)

# Define category columns for stacking
categories = col_names = df.columns[3:].values

# Define bar positions and model names
bar_positions = range(len(df))
model_names = df["model_name"]

# Define colors for each category
colors = ["yellowgreen", "gold", "orange", "tomato"]

# Create stacked horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bottom = [0] * len(df)

for idx, category in enumerate(categories):
    ax.barh(bar_positions, df[category], left=bottom, label=category, color=colors[idx])
    bottom = [b + v for b, v in zip(bottom, df[category])]

# Set labels and title
ax.invert_yaxis()
ax.set_yticks(bar_positions)
ax.set_yticklabels(model_names)
ax.set_xlabel("Lineage Benchmark Scores (stacked)")
ax.set_title("Lineage Benchmark Scores")
ax.legend(title="Problem Size")

# Add grid
ax.set_axisbelow(True)
ax.xaxis.grid(color='lightgray')

# Show plot
plt.tight_layout()

if output_file:
    plt.savefig(output_file)

plt.show()


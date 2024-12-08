import json
import matplotlib.pyplot as plt
import numpy as np

# Read the JSON file
with open('search_results.json', 'r') as json_file:
    search_results = json.load(json_file)

# Initialize sums and counts
algorithms = ['base', 'enhanced', 'levenshtein', 'jaro', 'soundex']
totals = {algo: {'returned_exact_match': 0, 'actual_exact_match': 0, 'time_of_execution': 0.0, 'search_result': 0} for algo in algorithms}
percentages = {algo: [] for algo in algorithms}
num_queries = len(search_results)

# Iterate over each query and accumulate the results
for word, results in search_results.items():
    for algo in algorithms:
        totals[algo]['returned_exact_match'] += results[algo]['returned_exact_match']
        totals[algo]['actual_exact_match'] += results[algo]['actual_exact_match']
        totals[algo]['time_of_execution'] += results[algo]['time_of_execution']
        totals[algo]['search_result'] += results[algo]['search_result']
        if results[algo]['actual_exact_match'] > 0:
            percentages[algo].append(results[algo]['returned_exact_match'] / results[algo]['actual_exact_match'])

# Calculate average percentages and times
averages = {algo: {} for algo in algorithms}
for algo in algorithms:
    averages[algo]['avg_percentage'] = sum(percentages[algo]) / len(percentages[algo]) if percentages[algo] else 0
    averages[algo]['avg_time'] = totals[algo]['time_of_execution'] / num_queries
    averages[algo]['avg_returned_results'] = totals[algo]['search_result'] / num_queries

# Data for plotting
categories = ['Avg. Returned %', 'Avg. Time (s)', 'Avg. Returned Results']
algo_names = ['Base', 'Enhanced', 'Levenshtein', 'Jaro', 'Soundex']
values = {
    'Avg. Returned %': [averages[algo]['avg_percentage'] for algo in algorithms],
    'Avg. Time (s)': [averages[algo]['avg_time'] for algo in algorithms],
    'Avg. Returned Results': [averages[algo]['avg_returned_results'] for algo in algorithms]
}

# Plotting
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

for i, category in enumerate(categories):
    axs[i].bar(algo_names, values[category], color=['blue', 'orange', 'green', 'red', 'purple'])
    axs[i].set_title(category)
    axs[i].set_ylabel('Value')
    axs[i].set_xlabel('Algorithm')

plt.tight_layout()
plt.show()

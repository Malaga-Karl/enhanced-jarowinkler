import json
import time
from titles import titles
from existing import ExistingAlgo
from enhanced import EnhancedAlgo
import re

def find_exact_matches(query, title):
    # Create a regex pattern to match exact words
    pattern = re.compile(r'\b' + re.escape(query.lower()) + r'\b')
    return bool(pattern.search(title.lower()))

def run_search(query, algo, mode):
    index_and_scores = dict()
    query_in_middle_of_string = []
    exact_matches = dict()
    start_time = time.time()

    for index, title in titles.items():
        score = algo.jaro_winkler(query.lower(), title.lower())
        if score >= 0.8:
            index_and_scores[index] = score
            if find_exact_matches(query, title):
                exact_matches[index] = score
        if find_exact_matches(query, title):
            query_in_middle_of_string.append(title)

    end_time = time.time()
    execution_time = end_time - start_time

    results = {
        'search_result': len(index_and_scores),
        'returned_exact_match': len(exact_matches),
        'actual_exact_match': len(query_in_middle_of_string),
        'time_of_execution': execution_time
    }

    return results

# Example array of search queries
queries = [
    "Complete Guide",
    "Quick Reference",
    "financial freedom",
    'For Adults',
    'Time Management',
    "Stress Relief",
    "Language Learning",
    "For Kids",
    "Guide to",
    "How to",
    "The Power"
]


# Initialize a dictionary to store results
all_results = {}

# Run the search for each query in both base and enhanced modes
for query in queries:
    base_results = run_search(query, ExistingAlgo, 'base')
    enhanced_results = run_search(query, EnhancedAlgo, 'enhanced')
    all_results[query] = {
        'base': base_results,
        'enhanced': enhanced_results
    }

# Save results to a JSON file
with open('search_results2.json', 'w') as json_file:
    json.dump(all_results, json_file, indent=4)

print("Results have been saved to search_results2.json")

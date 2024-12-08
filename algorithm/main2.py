import json
import time
from titles import titles
from existing import ExistingAlgo
from enhanced import EnhancedAlgo
import Levenshtein
from soundex import Soundex

def run_search(query, algo, mode):
    index_and_scores = dict()
    query_in_middle_of_string = []
    exact_matches = dict()
    start_time = time.time()

    for index, title in titles.items():
        score = algo.jaro_winkler(query.lower(), title.lower())
        if score >= 0.8:
            index_and_scores[index] = score
            if query.lower() in title.lower().split():
                exact_matches[index] = score
        if query.lower() in title.lower().split():
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

def run_lev(query):
    index_and_scores = dict()
    query_in_middle_of_string = []
    exact_matches = dict()
    start_time = time.time()

    for index, title in titles.items():
        score = Levenshtein.distance(query.lower(), title.lower())
        if score <= 3:
            index_and_scores[index] = score
            if query.lower() in title.lower().split():
                exact_matches[index] = score
        if query.lower() in title.lower().split():
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

def run_jaro(query):
    index_and_scores = dict()
    query_in_middle_of_string = []
    exact_matches = dict()
    start_time = time.time()

    for index, title in titles.items():
        score = Levenshtein.jaro(query.lower(), title.lower())
        if score >= 0.8:
            index_and_scores[index] = score
            if query.lower() in title.lower().split():
                exact_matches[index] = score
        if query.lower() in title.lower().split():
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

def run_soundex(query):
    sn = Soundex()
    index_and_scores = dict()
    query_in_middle_of_string = []
    exact_matches = dict()
    start_time = time.time()

    for index, title in titles.items():
        if sn.soundex_generator(query) == sn.soundex_generator(title):
            index_and_scores[index] = sn.soundex_generator(query)
            if query.lower() in title.lower().split():
                exact_matches[index] = sn.soundex_generator(query)
        if query.lower() in title.lower().split():
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
"time",
"year",
"people",
"way",
"day",
"man",
"thing",
"woman",
"life",
"child",
"world",
"school",
"state",
"family",
"student",
"group",
"country",
"problem",
"hand",
"part",
"place",
"case",
"week",
"company",
"system",
"program",
"question",
"work",
"government",
"number",
"night",
"point",
"home",
"water",
"room",
"mother",
"area",
"money",
"story",
"fact",
"month",
"lot",
"right",
"study",
"book",
"eye",
"job",
"word",
"business",
"issue",
"side",
"kind",
"head",
"house",
"service",
"friend",
"father",
"power",
"hour",
"game",
"line",
"end",
"member",
"law",
"car",
"city",
"community",
"name",
"president",
"team",
"minute",
"idea",
"kid",
"body",
"information",
"back",
"parent",
"face",
"others",
"level",
"office",
"door",
"health",
"person",
"art",
"war",
"history",
"party",
"result",
"change",
"morning",
"reason",
"research",
"girl",
"guy",
"moment",
"air",
"teacher",
"force",
"education"
]

# Initialize a dictionary to store results
all_results = {}

# Run the search for each query in both base and enhanced modes
for query in queries:
    base_results = run_search(query, ExistingAlgo, 'base')
    enhanced_results = run_search(query, EnhancedAlgo, 'enhanced')
    lev_results = run_lev(query)
    jaro_results = run_jaro(query)
    soundex_results = run_soundex(query)
    all_results[query] = {
        'base': base_results,
        'enhanced': enhanced_results,
        'levenshtein': lev_results,
        'jaro': jaro_results,
        'soundex': soundex_results
    }

# Save results to a JSON file
with open('search_results.json', 'w') as json_file:
    json.dump(all_results, json_file, indent=4)

print("Results have been saved to search_results.json")

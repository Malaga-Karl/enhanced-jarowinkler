import re
from titles import titles
from existing import ExistingAlgo
from enhanced import EnhancedAlgo
import Levenshtein

def find_exact_matches(query, title):
    # Create a regex pattern to match exact words
    pattern = re.compile(r'\b' + re.escape(query.lower()) + r'\b')
    return bool(pattern.search(title.lower()))

print("Enhanced Library Search Engine")
query = input("Search for a book: ")
mode = input("Enter Mode: [b]ase JW / [e]nhanced JW / [l]evenshtein: ")

index_and_scores = dict()
query_in_middle_of_string = []
exact_matches = dict()

if mode.lower() not in 'bel':
    quit()

# For Existing Jaro Searching
if mode.lower() == 'b':
    for index, title in titles.items():
        # Apply similarity score
        score = ExistingAlgo.jaro_winkler(query.lower(), title.lower())
        if score >= 0.8:
            index_and_scores[index] = score
            if find_exact_matches(query, title):
                exact_matches[index] = score

        # Check if query is in the middle of the string
        if find_exact_matches(query, title):
            query_in_middle_of_string.append(title)

# Enhanced Jaro Searching
elif mode.lower() == 'e':
    for index, title in titles.items():
        # Apply similarity score
        score = EnhancedAlgo.jaro_winkler(query.lower(), title.lower())
        if score >= 0.8:
            index_and_scores[index] = score
            if find_exact_matches(query, title):
                exact_matches[index] = score

        # Check if query is in the middle of the string
        if find_exact_matches(query, title):
            query_in_middle_of_string.append(title)

elif mode.lower() == 'l':
    for index, title in titles.items():
        # Apply similarity score
        score = Levenshtein.distance(query.lower(), title.lower())
        if score <= 3:
            index_and_scores[index] = score
            if find_exact_matches(query, title):
                exact_matches[index] = score

        # Check if query is in the middle of the string
        if find_exact_matches(query, title):
            query_in_middle_of_string.append(title)


sorted_index_and_scores = sorted(index_and_scores.items(), key=lambda item: item[1], reverse=True)

# Print the titles and their scores
print("Matching books and their scores:")
for index, score in sorted_index_and_scores:
    title = titles[index]
    print(f"{title}, Score: {score:.4f}")

print(f"\nsearch results {len(index_and_scores)}")
print(f"exact matches (from algorithm): {len(exact_matches)}")
print(f"'{query}' in the title {len(query_in_middle_of_string)}\n")

print("Exact Matches")
for title in query_in_middle_of_string:
    print(title)

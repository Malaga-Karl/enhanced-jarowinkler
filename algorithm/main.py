from titles import titles
from existing import ExistingAlgo
from enhanced import EnhancedAlgo

print("Enhanced Library Search Engine")
query = input("Search for a book: ")

index_and_scores = dict()

# for index, title in titles.items():
#     score = ExistingAlgo.jaro_winkler(query.lower(), title.lower())
#     if score >= 0.8:
#         index_and_scores[index] = score

for index, title in titles.items():
    score = EnhancedAlgo.jaro_winkler(query.lower(), title.lower())
    if score >= 0.8:
        index_and_scores[index] = score

sorted_index_and_scores = sorted(index_and_scores.items(), key=lambda item: item[1], reverse=True)

# Print the titles and their scores 
print("Matching books and their scores:") 
for index, score in sorted_index_and_scores: 
    title = titles[index] 
    print(f"{title}, Score: {score:.4f}")
def suffix_similarity(s1, s2, max_len=4):
    # Reverse the strings to compare suffixes as prefixes
    s1_reversed = s1[::-1]
    s2_reversed = s2[::-1]

    # Initialize the similarity count
    similarity_count = 0

    # Compare the characters from the reversed strings up to the max length
    for i in range(min(len(s1_reversed), len(s2_reversed), max_len)):
        if s1_reversed[i] == s2_reversed[i]:
            similarity_count += 1
        else:
            break

    return similarity_count


def multiTest():
    return 'Hello', 'Goodbye'

test, word = multiTest()

print(test, word)
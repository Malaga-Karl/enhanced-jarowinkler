def jaro_distance(s1: str, s2: str  ) -> tuple[float, int]:
    if s1 == s2:
        return 1.0
    
    len1, len2 = len(s1), len(s2)
    max_dist = max(len1, len2) // 2 - 1 # for symmetric peeking

    match = 0
    hash_s1 = [0] * len1
    hash_s2 = [0] * len2

    # for getting matches
    for i in range(len1):
        for j in range(max(0, i - max_dist), min(len2, i + max_dist + 1)):
            if s1[i] == s2[j] and hash_s2[j] == 0:
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break

    if match == 0:
        return 0.0

    # transposition
    t = 0
    point = 0

    for i in range(len1):
        if hash_s1[i]:
            while hash_s2[point] == 0:
                point += 1
            if s1[i] != s2[point]:
                t += 1
            point += 1

    t /= 2

    return (match / len1 + match / len2 + (match - t) / match) / 3.0, match


res = jaro_distance('diomedes', 'rafael')
print(res)
from existing import ExistingAlgo
from jarowinkler import *

word_pairs = [
    ["MARTHA", "MARHTA"],
    ["DWAYNE", "DUANE"],
    ["CRATE", "TRACE"],
    ["kitten", "sitting"],
    ["flaw", "lawn"],
    ["night", "nacht"],
    ["distant", "instance"],
    ["martha", "marhta"],
    ["jellyfish", "smellyfish"],
    ["abcdef", "abcfde"],
    ["apple", "apples"],
    ["michael", "mike"],
    ["saturday", "sundays"],
    ["paper", "piper"],
    ["lemon", "melon"],
    ["disaster", "distance"],
    ["butterfly", "flutterby"],
    ["autumn", "fall"],
    ["ballet", "ballets"],
    ["jungle", "jumble"]
]

for pair in word_pairs:
    if round(ExistingAlgo.jaro_distance(pair[0], pair[1]) , 4) == round(jaro_similarity(pair[0], pair[1]) , 4):
        print(f'✅ {pair} jaro match ')
    else:
        print(f'❌ {pair} jaro not match:\ncoded: {round(ExistingAlgo.jaro_distance(pair[0], pair[1]), 4)}\nlibrary: {round(jaro_similarity(pair[0], pair[1]), 4)}')

    if round(ExistingAlgo.jaro_winkler(pair[0], pair[1]) , 4) == round(jarowinkler_similarity(pair[0], pair[1]) , 4):
        print(f'✅ {pair} jarowinkler match ')
    else:
        print(f'❌ {pair} jarowinkler not match\ncoded: {round(ExistingAlgo.jaro_winkler(pair[0], pair[1]), 4)}\nlibrary: {round(jarowinkler_similarity(pair[0], pair[1]), 4)}')

    print()
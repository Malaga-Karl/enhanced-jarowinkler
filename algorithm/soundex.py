class Soundex:
    def __init__(self):
        None
    
    # soundex generator function
    def soundex_generator(self, token):
    
        # Convert the word to upper 
        # case for uniformity
        token = token.upper()
    
        soundex = ""
    
        # Retain the First Letter
        soundex += token[0]
    
        # Create a dictionary which maps 
        # letters to respective soundex
        # codes. Vowels and 'H', 'W' and
        # 'Y' will be represented by '.'
        dictionary = {"BFPV": "1", "CGJKQSXZ": "2",
                    "DT": "3",
                    "L": "4", "MN": "5", "R": "6",
                    "AEIOUHWY": "."}
    
        # Enode as per the dictionary
        for char in token[1:]:
            for key in dictionary.keys():
                if char in key:
                    code = dictionary[key]
                    if code != '.':
                        if code != soundex[-1]:
                            soundex += code
    
        # Trim or Pad to make Soundex a
        # 4-character code
        soundex = soundex[:7].ljust(7, "0")
    
        return soundex
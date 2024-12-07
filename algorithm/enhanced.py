class EnhancedAlgo:

    def jaro_winkler(s1, s2):

        def suffix_weight(s1: str, s2: str, m: int, prefix: int, jd: float) -> float:
            if(
                len(s1) > 5 and
                len(s2) > 5 and
                m - prefix >= 2 and
                m - prefix >= min(len(s1), len(s2)) // 2
            ):
                s1Reversed = s1[::-1]
                s2Reversed = s2[::-1]

                suffix_count = 0
                for i in range(min(len(s1Reversed), len(s2Reversed), 4)):
                    if s1Reversed[i] == s2Reversed[i]:
                        suffix_count += 1
                    else:
                        break
                return jd + suffix_count * 0.1 * (1-jd)
            else:
                return 0.1
                

        # Jaro distance calculation
        def jaro_distance(s1: str, s2: str) -> tuple[float, int]:
            if s1 == s2:
                return 1.0, len(s1)
            
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
                return 0.0, match

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

            jd = (match / len1 + match / len2 + (match - t) / match) / 3.0
            return jd, match
        
        # Rolling Jaro-Winkler distance calculation

        maxJw = 0.1
        s1Split = s1.split()
        s2Split = s2.split()


        for i in range(len(s2Split)):
            # groups referent according to length of words of target
            s2group = ' '.join(s2Split[i: i + len(s1Split)])

            jaro_dist, match = jaro_distance(s1, s2group)

            prefix = 0
            for i in range(min(len(s1), len(s2group))):
                if s1[i] == s2[i]:
                    prefix += 1
                else:
                    break

            prefix = min(4, prefix)
            jw = jaro_dist + 0.1 * prefix * (1 - jaro_dist)
            # if jw > 0.80:
            #     return jw
            if jw > maxJw:
                maxJw = jw
            jw = suffix_weight(s1, s2, match, prefix, jaro_dist)
            if jw > maxJw:
                maxJw = jw
                
        return maxJw



    


    def jaro_distance(s1, s2):
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

            return (match / len1 + match / len2 + (match - t) / match) / 3.0
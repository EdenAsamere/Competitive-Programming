from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)  
        first_window = s[:k]
        i = 0
        pdict = Counter(p)
        sdict = Counter(first_window)
        indices = []
        if sdict == pdict:
            indices.append(i)
        for j in range(k, len(s)):
            sdict[s[i]] -= 1
            if sdict[s[i]] == 0:
                del sdict[s[i]]
            sdict[s[j]] += 1
            i += 1
            if sdict == pdict:
                indices.append(i)
        return indices

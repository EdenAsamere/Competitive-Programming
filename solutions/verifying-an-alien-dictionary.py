class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words_map = {}
        for i, j in enumerate(order):
            words_map[j] = i
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if words_map[word1[j]] > words_map[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        
        return True

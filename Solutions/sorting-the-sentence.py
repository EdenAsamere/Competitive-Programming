class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split()
        shuffled = [''] * len(splitted)
        for word in splitted:
            wonum = word.strip(word[-1])
            shuffled[int(word[-1]) - 1] = wonum
        return ' '.join(shuffled)
        
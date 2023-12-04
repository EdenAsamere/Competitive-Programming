class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mer =""
        for i,j in list(zip(word1,word2)):
            mer +=(i+j)
        if len(word1) > len(word2):
            mer+=word1[len(word2):]
        else:
            mer+=word2[len(word1):]
        return mer


        
class Solution:
    def restoreString(self,s, indices):
        shuffled = [''] *len(s)
        for i,j in enumerate(s):
            shuffled[indices[i]] = j
        shuffled_string = ''.join(shuffled)
        return shuffled_string 
                
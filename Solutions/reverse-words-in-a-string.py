class Solution:
    def reverseWords(self, s: str) -> str:
        o = s.split(' ')
        k =[x for x in o if x != '']
        i = 0
        j = len(k) -1
        while i < j:
            k[i],k[j] = k[j],k[i]
            i +=1
            j-=1
        return " ".join(k)
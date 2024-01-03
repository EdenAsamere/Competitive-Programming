class Solution:
    def isPalindrome(self, s: str) -> bool:
        string =''.join(i for i in s if i.isalnum()).lower()
        i = len(string)-1
        for j in range(len(string)):
            if i < len(string) and string[j] != string[i]:
                return False        
            i-=1
        return True
            
                
                       
            
        
        
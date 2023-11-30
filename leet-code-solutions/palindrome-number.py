class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:return False
        rev=0
        num = x
        while x != 0:
            dig = x % 10
            rev = rev * 10 + dig
            x//=10
        return num == rev    
         
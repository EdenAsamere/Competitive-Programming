class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        while n!=1:
            if n % 2 :
                matches = (n-1)//2
                advance = (n-1)//2+1
            else:
                matches = n//2
                advance = n//2
            total_matches+=matches   
            n = advance
        return total_matches
        
            
        
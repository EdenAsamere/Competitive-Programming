class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ter = ""
        while n!=0:
            rem = n % 3
            ter+=str(rem)
            n = n //3
        return "2" not in ter
            
        
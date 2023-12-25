class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        answer = []
        for i in digits:
            number = number*10 + i  
        number +=1
        while number != 0:
            digit = number % 10
            answer.append(digit)
            number//=10
        return answer[::-1]
            
            
            
            

        
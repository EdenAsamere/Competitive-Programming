class Solution:
    def isHappy(self, n: int) -> bool:
        nums_set = set()  
        while n != 1 :
            temp = 0
            nums_list = return_digits(n)
            for i in nums_list:
                temp += (i**2)
            n = temp
            if n in nums_set:
                return False
            nums_set.add(n)
        return True
    
def return_digits(n):
    digits = []
    num = n
    while num!=0:
        dig = num%10
        digits.append(dig)    
        num //= 10
    return digits
            
            
    
            
            
            
        
        
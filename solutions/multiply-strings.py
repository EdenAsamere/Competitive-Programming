class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        new_string = num1 + "*" +num2
        return str(eval(new_string))
        
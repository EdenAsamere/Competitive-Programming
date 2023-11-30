class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return [int((num/3)-1),int((num/3)),int((num/3)+1)] if num/3 == num//3 else []
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = len(numbers)-1
        j = 0
        while i > 0 and j < len(numbers):
            if numbers[j] + numbers[i] == target:
                return [j+1,i+1]
            elif numbers[j] + numbers[i] < target:
                j +=1
            else:
                i -=1
        return []


        
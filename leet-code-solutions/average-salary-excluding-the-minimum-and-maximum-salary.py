class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        include = salary[1:len(salary)-1]
        return sum(include)/len(include)
        
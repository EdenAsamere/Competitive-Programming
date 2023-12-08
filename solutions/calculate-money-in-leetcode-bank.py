class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        remaining_days = n % 7
        total_sum = 0
        for i in range(full_weeks):
            total_sum += 7 *(4+i)      
        for i in range(remaining_days):
            total_sum += (i + 1 + full_weeks)
        return total_sum

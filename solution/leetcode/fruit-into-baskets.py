from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = 0
        basket = defaultdict(int)
        p = 0
        for i, value in enumerate(fruits):
            basket[value] += 1
            while  len(basket) > 2:
                basket[fruits[p]] -= 1
                if basket[fruits[p]] == 0:
                    del basket[fruits[p]]
                p += 1
            window = max(window, i - p + 1)
        return window

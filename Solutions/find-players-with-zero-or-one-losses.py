from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = ([i[0] for i in matches])
        losers = [i[1] for i in matches]
        loser_counter = Counter(losers)
        return [sorted(list(set(winners)-set(losers))),sorted([i for i,j in loser_counter.items() if j == 1])]

        
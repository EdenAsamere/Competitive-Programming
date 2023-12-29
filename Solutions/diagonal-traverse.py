from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dictionary = defaultdict(list)
        result = []

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                dictionary[row + col].append(mat[row][col])

        for key in dictionary:
            if key % 2:
                result.extend(dictionary[key])
            else:
                result.extend(list(reversed(dictionary[key])))
        return result

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp = [[0] * len(matrix) for i in range(len(matrix[0]))]
        for rows in range(len(matrix)):
             for cols in range(len(matrix[0])):
                    temp[cols][rows] = matrix[rows][cols]
        return temp
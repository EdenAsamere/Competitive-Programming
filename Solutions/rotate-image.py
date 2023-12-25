import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = copy.deepcopy(matrix)
        for rows in range(len(matrix)):
            for cols in range(len(matrix)):
                matrix[rows][cols] = temp[cols][rows]
        for rows in range(len(matrix)):
            matrix[rows] = matrix[rows][::-1]  
        return matrix

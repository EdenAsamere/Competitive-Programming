class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        store_visited = set()
        diagonal_sum = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row == col:
                    store_visited.add((row,col))
                    diagonal_sum += mat[row][col]
                if row + col == len(mat) -1 and (row,col) not in store_visited:
                    diagonal_sum += mat[row][col]
        return diagonal_sum
                    
                
        
        
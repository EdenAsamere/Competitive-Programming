class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count =0
        for col in range(len(strs[0])):
            column_elements = []
            for row in range(len(strs)):
                column_elements.append(strs[row][col])
            if sorted(column_elements) != column_elements:
                count +=1
        return count

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        word_dictionary = {}
        output = []
        min_index_sum = float('inf')
        
        for i, j in enumerate(list1):
            word_dictionary[j] = i
        
        for i, j in enumerate(list2):
            if j in word_dictionary.keys():
                current_index_sum = word_dictionary[j] + i
                if current_index_sum < min_index_sum:
                    min_index_sum = current_index_sum
                    output = [j]
                elif current_index_sum == min_index_sum:
                    output.append(j)
        
        return output

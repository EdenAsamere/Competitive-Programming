from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {j: i for i, j in enumerate(arr2)}
        def customComparator(item):
            return hashmap[item] if item in hashmap else len(arr2) + item
        arr1.sort(key=customComparator)
        return arr1

        
        
        
        
        
        # hashmap = Counter(arr1)
        # output = []
        # for i in arr2:
        #     output.extend([i]*hashmap[i])
        # diff = sorted(list( set(arr1) - set(arr2)))
        # for i in diff:
        #     output.extend([i]*hashmap[i])
        # return output
        
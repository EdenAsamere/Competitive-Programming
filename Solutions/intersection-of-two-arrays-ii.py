from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dic = Counter(nums1)
        nums2_dic = Counter(nums2)
        answer = []
        for key in (set(nums1_dic) & set(nums2_dic)):
            answer.extend([key] * min(nums1_dic[key], nums2_dic[key]))
        return answer

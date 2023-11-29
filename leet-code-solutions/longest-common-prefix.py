class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a = strs[0]
        b = strs[-1]
        pre = ''
        for i in range(min(len(a),len(b))):
            if a[i]!=b[i]:
                return pre
            pre+=a[i]
        return pre
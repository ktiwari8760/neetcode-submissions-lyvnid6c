class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        strs.sort()
        num1 = strs[0]
        nums2 = strs[-1]
        common_prefix = ""

        for i in range(min(len(num1) , len(nums2))):
            if num1[i] != nums2[i]:
                break
            common_prefix += num1[i]
        return common_prefix
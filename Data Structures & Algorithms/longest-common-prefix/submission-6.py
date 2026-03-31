class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first_ele = strs[0]
        last_ele = strs[-1]
        common_prefix = ""
        left = 0
        while(left < min(len(first_ele ) , len(last_ele))):
            if first_ele[left] == last_ele[left]:
                common_prefix += first_ele[left]
                left+=1
            else:
                break
        return common_prefix


        


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare_string = strs[0]
        common_prefix = ""
        for i ,ele in enumerate(compare_string):
            flag = False
            for element in strs:
                print(element , ele)
                if element[i] != ele:
                    flag = True
                    break
            if flag:
                break
            else:
                common_prefix += ele
        return common_prefix


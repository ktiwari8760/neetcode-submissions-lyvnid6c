class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for ele in strs:
            sorted_ele = "".join(sorted(ele))
            hash[sorted_ele] = hash.get(sorted_ele , []) + [ele]  
        return list(hash.values())
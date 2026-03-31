class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in range(len(strs)):
            count = [0] * 26
            for c in strs[i]:
                count[ord(c)-ord('a')] += 1
            sum1 = tuple(count)
            if sum1 in dict1:
                dict1[sum1].append(strs[i])
            else:
                dict1[sum1] = [strs[i]]
        return list(dict1.values())
        
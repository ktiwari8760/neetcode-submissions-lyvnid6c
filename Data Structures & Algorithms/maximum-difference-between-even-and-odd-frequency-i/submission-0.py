class Solution:
    def maxDifference(self, s: str) -> int:
        hash = {}
        for ele in s:
            hash[ele] = hash.get(ele , 0) + 1
        min_even = float('inf')
        max_odd = float('-inf')
        for ele in hash.values():
            if ele % 2 == 0:
                min_even = min(min_even , ele)
            else:
                max_odd = max(max_odd , ele)
        return max_odd - min_even
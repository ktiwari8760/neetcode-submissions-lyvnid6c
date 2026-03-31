class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = float('-inf')
        for ele in nums:
            if ele+1 in nums:
                continue
            length = 0
            while(ele-1 in nums):
                length += 1
                ele = ele-1
            max_length = max(max_length , length)
        return max_length+1 if max_length != float('-inf') else 0

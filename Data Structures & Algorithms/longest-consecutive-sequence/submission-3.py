class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        max_length = 0
        for ele in nums:
            if ele-1 in hash:
                continue
            else:
                length = 1
                while(ele+1 in hash):
                    length += 1
                    ele += 1
                max_length = max(max_length , length)
        return max_length

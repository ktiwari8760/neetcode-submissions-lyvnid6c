class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums = set(nums)
        for ele in nums:
            if ele-1 in nums:
                continue
            else:
                counter = 0
                temp = ele
                while temp in nums:
                    counter += 1
                    temp += 1
            max_length = max(max_length , counter)
        return max_length
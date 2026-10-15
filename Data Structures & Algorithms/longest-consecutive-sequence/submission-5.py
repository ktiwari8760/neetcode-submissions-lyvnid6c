class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_counter = 0
        for ele in nums:
            if ele - 1 in nums_set:
                continue
            else:
                temp = ele
                counter= 0 
                while temp in nums_set:
                    counter += 1
                    temp += 1
                max_counter = max(max_counter , counter)
        return max_counter
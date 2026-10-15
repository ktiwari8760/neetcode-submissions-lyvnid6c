class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # This will help us with o(1) searches
        max_counter = 0 # This cannot be negative hence 0 could have been 1 too
        for ele in nums:
            if ele - 1 in nums_set:
                # If lower element exists means it's not the starting 
                continue
            else:
                # This is the starting of the sequence we check it's length
                temp = ele
                counter= 0 
                while temp in nums_set:
                    counter += 1
                    temp += 1
                max_counter = max(max_counter , counter)
        return max_counter
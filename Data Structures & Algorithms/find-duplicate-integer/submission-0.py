class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()

        for ele in nums:
            if ele in hashset:
                return ele
            hashset.add(ele)
        return -1
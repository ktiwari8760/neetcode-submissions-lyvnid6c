class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for ele in nums:
            hash[ele] = hash.get(ele , 0) + 1
        
        for key , value in hash.items():
            if value != 1:
                return True
        return False
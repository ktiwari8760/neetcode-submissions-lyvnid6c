class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = Counter(nums)
        
        for key , value in hash.items():
            if value != 1:
                return True
        return False
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = 0
        hashset = set()   # Window
        while(right < len(nums)):
            if nums[right] in hashset:
                return True
            if right-left >= k:
                hashset.remove(nums[left])
                left += 1
            hashset.add(nums[right])
            right += 1
        return False
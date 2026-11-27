class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()
        if k == 0:
            return False
        for right in range(len(nums)):
            if nums[right] in window:
                return True
            else:
                while (right-left) >= k:
                    window.discard(nums[left])
                    left += 1
            window.add(nums[right])
        return False
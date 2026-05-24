class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        answer= []
        while(right <= len(nums)):
            sub_array = nums[left:right]
            answer.append(max(sub_array))
            left += 1
            right += 1
        return answer

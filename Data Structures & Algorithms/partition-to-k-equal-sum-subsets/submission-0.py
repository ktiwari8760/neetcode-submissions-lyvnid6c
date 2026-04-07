class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summing = sum(nums) / k
        summation = [0] * k
        nums.sort(reverse = True)
        def helper(index):
            nonlocal summation
            if index == len(nums):
                return True
            
            for j in range(k):
                if summation[j] + nums[index] <= summing:
                    summation[j] += nums[index]
                    if helper(index+1):
                        return True
                    summation -= nums[index]
            return False
        return helper(0)
                
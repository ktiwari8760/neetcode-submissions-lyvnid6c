class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        # If total not divisible by k → impossible
        if total % k != 0:
            return False

        summing = total // k        
        summation = [0] * k
        nums.sort(reverse = True)
        def helper(index):
            nonlocal summation
            if index == len(nums):
                return True
            if index > len(nums):
                return False
            for j in range(k):
                if summation[j] + nums[index] <= summing:
                    summation[j] += nums[index]
                    if helper(index+1):
                        return True
                    summation[j] -= nums[index]
            return False
        return helper(0)
                
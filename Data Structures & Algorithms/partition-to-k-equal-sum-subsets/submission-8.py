class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        nums.sort(reverse = True)
        if total % k != 0:
            return False
        target = total // k
        if any( ele > target for ele in nums):
            return False
        sides = [0] * k
        def helper(index , sides):
            if index == len(nums):
                return all(ele == target for ele in sides)
            if any(ele > target for ele in sides):
                return False
            for i in range(len(sides)):
                if i > 0 and sides[i] == sides[i - 1]:
                    continue
                if sides[i] < target and sides[i] + nums[index] <= target:
                    sides[i] += nums[index]
                    if helper(index+1 , sides):
                        return True
                    sides[i] -= nums[index]
                else:
                    continue
            return False
        return helper(0 , sides)

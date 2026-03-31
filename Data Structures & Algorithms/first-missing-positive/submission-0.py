class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i , ele in enumerate(nums):
            if ele < 0:
                nums[i] = 0
        print(nums)
        for i , ele in enumerate(nums):
            if ele != 0 :
                index = abs(ele)-1
                if index < 0 or index > len(nums)-1:
                    continue
                else:
                    if nums[index] > 0:
                        nums[index] = -1 * nums[index]
                    elif nums[index] == 0:
                        nums[index] = -1 * (len(nums)+1)
        print(nums)
        for i in range(1 , len(nums)+1):
            index = i - 1
            if nums[index] >= 0:
                return i
        return len(nums)+1

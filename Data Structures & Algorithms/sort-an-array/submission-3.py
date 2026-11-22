class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quick_sort(nums):
            if not nums:
                return []
            left = 0
            right = len(nums)-1
            pivot = (left + right) //2
            mid = nums[pivot]
            l , e , r = [] , [] , []
            for i in range(len(nums)):
                if nums[i] < mid:
                    l.append(nums[i])
                elif nums[i] > mid:
                    r.append(nums[i])
                else:
                    e.append(nums[i])
            return quick_sort(l) + e + quick_sort(r)
        
        return quick_sort(nums)
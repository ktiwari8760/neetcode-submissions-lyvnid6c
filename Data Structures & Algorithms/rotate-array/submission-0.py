class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def function(nums , left , right):
            while(left <= right):
                nums[left] , nums[right] = nums[right] , nums[left]
                left +=1
                right -= 1

        # Reverse entire array
        function(nums , 0 , len(nums)-1)
        function(nums , 0 , k-1)
        function(nums , k , len(nums)-1)
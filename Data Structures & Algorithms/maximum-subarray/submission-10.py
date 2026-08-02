class Solution:
    def maxSubArray(self, arr: List[int]) -> int:

        sum_ = 0
        max_sum = float('-inf')
        for i in range(len(arr)):
            sum_ += arr[i]

            if sum_ < arr[i]:
                sum_ = arr[i]
            max_sum = max(max_sum , sum_)
        return max_sum

class NumArray:

    def __init__(self, nums: List[int]):
        counter = 0
        self.prefix_sum = []
        for ele in nums:
            counter += ele
            self.prefix_sum.append(counter)
        print(self.prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix_sum[left-1] if left > 0 else 0
        return self.prefix_sum[right]-left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
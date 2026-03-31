class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = {}

        for ele in nums:
            dict_[ele] = dict_.get(ele , 0) + 1

        for key , value in dict_.items():
            if value > len(nums)/2:
                return key
        return -1
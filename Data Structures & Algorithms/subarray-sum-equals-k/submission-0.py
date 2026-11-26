class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currsum = 0
        prefixsum = {0 : 1}

        for i in range(len(nums)):
            currsum += nums[i]
            req = currsum-k

            if req in prefixsum.keys():
                res += prefixsum.get(req)
            prefixsum[currsum] = prefixsum.get(currsum , 0)+1
        return res
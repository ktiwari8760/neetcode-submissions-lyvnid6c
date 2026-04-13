class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half_sum = sum(nums)/2
        hash = {}
        def df(index , summation):
            if summation == half_sum:
                return True
            if summation > half_sum:
                return False
            if index > len(nums)-1:
                return False
            if (index , summation) in hash:
                return hash[(index , summation)]
            hash[(index , summation)] = False
            if df(index+1 , summation + nums[index]):
                hash[(index , summation)] = True
                return True
            if df(index+1 , summation ):
                hash[(index , summation)] = True
                return True
            return False
        return df(0 , 0)
            

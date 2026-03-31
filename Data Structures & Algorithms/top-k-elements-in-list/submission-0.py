class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need an array of arrays of length len(nums)+1
        arr = [[] for i in range(len(nums)+1)]

        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1.keys():
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
        
        for number , frequency in dict1.items():
            arr[frequency].append(number)
        
        result = []
        for i in range(len(arr)-1 , -1, -1):
            for num in arr[i]:
                result.append(num)
                if len(result) == k:
                    return result



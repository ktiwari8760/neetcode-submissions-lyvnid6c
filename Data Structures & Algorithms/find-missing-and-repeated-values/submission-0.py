class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = []
        for ele in grid:
            arr.extend(ele)
        repeating = []
        for i , ele in enumerate(arr):
            index = abs(ele)-1
            if arr[index] < 0:
                repeating.append(index+1)
            arr[index] = abs(arr[index]) * -1
        missing = []
        for i , ele in enumerate(arr):
            if ele > 0:
                missing.append(i+1)
        print(missing , repeating)
        return [repeating[0] , missing[0]]
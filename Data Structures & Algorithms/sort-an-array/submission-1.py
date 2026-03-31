class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def sort(arr):
            if len(arr) == 1:
                return arr
            if not arr:
                return []
            pivot = len(arr)//2
            pivot_ele = arr[pivot]

            left = []
            right = []
            middle = []
            for ele in arr:
                if ele < pivot_ele:
                    left.append(ele)
                elif ele == pivot_ele:
                    middle.append(ele)
                else:
                    right.append(ele)

            return sort(left) + middle + sort(right)
        return sort(nums)
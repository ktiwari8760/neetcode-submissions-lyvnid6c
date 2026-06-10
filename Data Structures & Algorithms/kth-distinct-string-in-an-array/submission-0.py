class Solution:
    def kthDistinct(self, nums: List[str], k: int) -> str:
        arr = []
        from collections import Counter
        hash = Counter(nums)

        for ele in nums:
            if hash[ele] == 1:
                arr.append(ele)
        print(arr)
        return arr[k-1] if k-1 < len(arr) else ""

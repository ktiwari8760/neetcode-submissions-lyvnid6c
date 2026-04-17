class Solution:
    def topKFrequent(self, nums: List[int], a: int) -> List[int]:
        dict_ = {}
        for ele in nums:
            dict_[ele] = dict_.get(ele , 0) + 1
        arr = [[] for _ in range(len(nums))]
        for k , v in dict_.items():
            v = v-1
            if arr[v] == []:
                arr[v] = [k]
            else:
                arr[v].append(k)
        topk = []
        for i in range(len(arr)-1 , -1 , -1):
            if len(arr[i]) > 0:
                topk.extend(arr[i])
        return topk[:a]
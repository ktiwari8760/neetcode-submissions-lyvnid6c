class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TOP K Frequent element
        hash = {}
        for ele in nums:
            hash[ele] = hash.get(ele , 0) + 1
        arr = [[] for i in range(len(nums)+1)]
        for key , value in hash.items():
            arr[value].append(key)
        answer = []
        for i in range(len(arr)-1 , -1 , -1):
            if arr[i]:
                answer.extend(arr[i])
        print(answer)
        return answer[:k][::-1]

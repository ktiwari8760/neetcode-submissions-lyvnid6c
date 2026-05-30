class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for ele in nums:
            hash[ele] = hash.get(ele , 0) + 1
        arr = [(-v , k) for k , v in hash.items()]
        heapq.heapify(arr)
        answer = []
        while k:
            freq , value = heapq.heappop(arr)
            answer.append(value)
            k -= 1
        return answer
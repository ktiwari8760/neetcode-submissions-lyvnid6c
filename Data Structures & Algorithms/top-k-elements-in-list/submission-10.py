class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We approach this problem using heap

        hash_freq = Counter(nums)

        heap = []
        heapq.heapify(heap)

        for key , value in hash_freq.items():
            heapq.heappush(heap , (-value , key))
        answer = []
        while k:
            freq , value = heapq.heappop(heap)
            answer.append(value)
            k -= 1
        return answer
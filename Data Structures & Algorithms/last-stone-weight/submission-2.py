class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for ele in stones:
            heapq.heappush(heap , -ele)
        
        while(heap and len(heap) != 1):
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y:
                heapq.heappush(heap , 0)
            else:
                heapq.heappush(heap , -abs(x-y))
        return -heap[0]
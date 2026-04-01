class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heap.append((-a , "a"))
        if b > 0:
            heap.append((-b , "b"))
        if c > 0:
            heap.append((-c , "c"))
        heapq.heapify(heap)
        result = []
        while(len(heap) > 0):
            count , ch = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == ch and result[-2] == ch :
                if not heap:
                    break
                count2 , ch2 = heapq.heappop(heap)
                result.append(ch2)
                count2 += 1
                if count2 < 0:
                    heapq.heappush(heap , (count2 , ch2))
                if count < 0:
                    heapq.heappush(heap , (count , ch))
            else:
                result.append(ch)
                count += 1
                if count < 0:
                    heapq.heappush(heap , (count , ch))
        return "".join(result)

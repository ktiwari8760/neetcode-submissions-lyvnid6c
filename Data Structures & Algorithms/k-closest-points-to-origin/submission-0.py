class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def calculatedistance(point):
            x1 = point[0]
            y1 = point[1]
            return ((x1 ** 2) + (y1 ** 2)) ** 0.5
        
        for point in points:
            distance = calculatedistance(point)
            heapq.heappush(heap , (distance , point))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
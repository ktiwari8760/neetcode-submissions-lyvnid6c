class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        leftcapacity = capacity
        heap = []
        for trip in trips:
            heap.append((trip[1] , (trip[0] , trip[2])))
        heapq.heapify(heap)
        map = {}
        while(heap):
            popped = heapq.heappop(heap)
            frompos = popped[0] 
            passenger , topos = popped[1] 
            for key , val in map.items():
                if key <= frompos:
                    leftcapacity += val
            if leftcapacity < passenger:
                return False
            leftcapacity -= passenger
            if topos in map.keys():
                map[topos] += passenger
            else:
                map[topos] = passenger
        return True

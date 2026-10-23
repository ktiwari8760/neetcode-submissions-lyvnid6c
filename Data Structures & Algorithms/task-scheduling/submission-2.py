class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash = Counter(tasks)
        heap = []
        heapq.heapify(heap)

        for key , value in hash.items():
            heapq.heappush(heap , (-value , key))
        
        timer = 0
        queue = deque([])

        while heap or queue:
            # we check if heap has any value
            if heap:
                freq , ele = heapq.heappop(heap)
                freq += 1
                if freq < 0:
                    queue.append((freq , ele , timer))
            if queue:
                while queue and queue[0][2] + n <= timer:
                    freq , ele , t = queue.popleft()
                    heapq.heappush(heap , (freq , ele))
            timer += 1
        return timer


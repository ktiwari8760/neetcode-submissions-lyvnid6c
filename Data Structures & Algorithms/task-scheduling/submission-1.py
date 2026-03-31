class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [0] * 26
        for ele in tasks:
            heap[ord(ele) - ord('A')] += 1
        heap = [-f for f in heap if f > 0]
        queue = deque()
        time = 0
        heapq.heapify(heap)
        while queue or heap:
            if not heap:
                time = queue[0][1]
                heapq.heappush(heap , queue.popleft()[0])
            time += 1
            count = heapq.heappop(heap)+1
            if count < 0:
                queue.append((count , time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap , queue.popleft()[0])
        return time
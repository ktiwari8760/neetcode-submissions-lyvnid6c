class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = [0] * 26
        for ele in tasks:
            index = ord(ele) - ord('A')
            task_freq[index] += 1
        print(task_freq) # Array containing frequency for the tasks
        task_freq = [-f for f in task_freq if f > 0]
        heapq.heapify(task_freq)
        queue = deque()
        time = 0

        while queue or task_freq:
            if not task_freq:
                time = queue[0][1]
                heapq.heappush(task_freq , queue.popleft()[0])
            time += 1
            count = heapq.heappop(task_freq)+1
            if count < 0:
                queue.append((count , time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(task_freq ,queue.popleft()[0])
        return time
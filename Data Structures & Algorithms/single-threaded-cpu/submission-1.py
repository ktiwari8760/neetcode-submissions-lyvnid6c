class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort the tasks according to time

        interval_task = sorted(enumerate(tasks) , key = lambda x : x[1][0])

        answer = []
        runs = []
        i = 0
        current_time = 0
        while len(answer) < len(tasks):
            while i < len(interval_task) and interval_task[i][1][0] <= current_time:
                index , (_ , execution_time) = interval_task[i]
                heapq.heappush(runs , (execution_time , index))
                i += 1
            if runs:
               execution_time ,  index = heapq.heappop(runs)
               current_time += execution_time
               answer.append(index)
            else:
                current_time = interval_task[i][1][0]
        return answer
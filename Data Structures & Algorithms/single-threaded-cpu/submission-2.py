class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # Sort the array of tasks and also enumerate it to preserve it's order

        tasks = [(i , task) for i , task in enumerate(tasks)]
        tasks.sort(key = lambda x : x[1][0])

        # Here my task is kind of sorted as well as enumerated with actual numbers

        # Now I start a loop where I will continue it until i process all tasks
        answer = [] # Processed tasks array
        i = 0
        current_time = 0
        runs = []
        heapq.heapify(runs)
        while(len(answer) < len(tasks)):
            while i < len(tasks) and tasks[i][1][0] <= current_time:
                index ,( _ , processing_time) = tasks[i]
                heapq.heappush(runs , (processing_time , index))
                i += 1
            if runs:
                processing_time , index = heapq.heappop(runs)
                current_time += processing_time
                answer.append(index)
            else:
                current_time = tasks[i][1][0]
        return answer
        

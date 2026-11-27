class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[1])

        answer = []

        for i in range(len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            while answer and answer[-1][1] >= s and answer[-1][0] < e:
                start , end = answer.pop()
                s = min(s , start)
                e = max(e , end)
            answer.append([s , e])
        
        return answer

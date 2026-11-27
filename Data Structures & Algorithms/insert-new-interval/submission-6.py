class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            if end < newInterval[0]:
                answer.append([start, end])
                i += 1
            else:
                break
        
        while i < len(intervals) and intervals[i][1] >= newInterval[0] and  intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0] , newInterval[0])
            newInterval[1] = max(intervals[i][1] , newInterval[1])
            i+=1
        
        answer.append(newInterval)

        while i < len(intervals):
            answer.append(intervals[i])
            i += 1
        
        return answer
        


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        print(intervals)
        output = [intervals[0]]
        for i , interval in enumerate(intervals[1:]):
            if output[-1][1] >= interval[0]:
                newInterval = [min(output[-1][0] , interval[0]) , max(output[-1][1] , interval[1])]
                output.pop()
                output.append(newInterval)
            else:
                output.append(interval)
        return output


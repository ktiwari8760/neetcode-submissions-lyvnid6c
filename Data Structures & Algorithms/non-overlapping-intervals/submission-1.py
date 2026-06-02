class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])

        end = intervals[0][1]
        counter = 0
        for i , interval in enumerate(intervals[1:]):
            if interval[0] >= end and interval[1] >= end:
                end = interval[1]
            else:
                counter += 1
                end = min(end , interval[1])
        return counter
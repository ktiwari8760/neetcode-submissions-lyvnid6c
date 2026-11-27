class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        intervals.sort(key = lambda x : x[0])
        prev_end = intervals[0][1]
        for i in range(1 , len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if s < prev_end:
                prev_end = min(prev_end , e)
                count += 1
            else:
                prev_end = e
        return count
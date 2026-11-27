"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = [[x.start , x.end]for x in intervals]
        intervals.sort(key = lambda x : x[1] )
        if len(intervals) == 0:
            return True
        prev_End = intervals[0][1]
        for i in range(1 , len(intervals)):
            start = intervals[i][0]
            if start < prev_End:
                return False
            prev_End = intervals[i][1]
        return True
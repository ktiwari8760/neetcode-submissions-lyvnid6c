"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:   
        if not intervals or len(intervals) == 0:
            return True
        temp = [[interval.start , interval.end] for interval in intervals]
        temp.sort(key = lambda x : x[0])
        intervals = temp.copy()
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        for start , end in intervals[1:]:
            if start < prev_end and end > prev_start:
                return False
            prev_start = start
            prev_end = end
        return True
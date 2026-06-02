"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        
        for i in range(len(intervals)-1):
            interval_1 = intervals[i]
            interval_2 = intervals[i+1]
            if interval_1.end > interval_2.start and interval_1.start < interval_2.end:
                return False
        return True
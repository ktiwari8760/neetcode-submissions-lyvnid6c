"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : x.start)
        if len(intervals) < 1:
            return 0
        rooms = [[intervals[0]]]
        for i in range(1 , len(intervals)):
            inserted = False
            for room in rooms:
                interval_1 = room[-1]
                interval_2 = intervals[i]
                if interval_1.end > interval_2.start and interval_1.start < interval_2.end:
                    continue
                else:
                    room.append(interval_2)
                    inserted = True
                    break
            if not inserted:
                rooms.append([intervals[i]])
        return len(rooms)

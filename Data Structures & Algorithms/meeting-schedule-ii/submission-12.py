"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]

        start.sort()
        end.sort()

        s = 0
        e = 0
        count = 0
        max_count = 0
        while(s < len(start) and e < len(end)):
            if start[s] < end[e]:
                s += 1
                count += 1
            elif end[e] < start[s]:
                e += 1
                count -= 1
            else:
                s += 1
                e += 1
            max_count = max(max_count , count)
        return max_count

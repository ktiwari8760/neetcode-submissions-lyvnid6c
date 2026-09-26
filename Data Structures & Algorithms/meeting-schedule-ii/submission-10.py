"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals or len(intervals) == 0:
            return 0
        temp = [[interval.start , interval.end] for interval in intervals]
        temp.sort(key = lambda x : x[0])
        intervals = temp.copy()
        room_engagement = 1
        room_engagement_time = [temp[0][1]]
        heapq.heapify(room_engagement_time)
        for start , end in intervals[1:]:
            min_engagement = room_engagement_time[0]
            if start < min_engagement:
                room_engagement += 1
                heapq.heappush(room_engagement_time , end)
            else:
                heapq.heapreplace(room_engagement_time , end)
        return room_engagement
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
        rooms = [[] for _ in intervals]
        for interval in intervals:
            start = interval.start
            end = interval.end
            print(start , end)
            for room in rooms:
                if not room:
                    room.append([start , end])
                    break
                else:
                    if room[-1][1] <= start:
                        room.append([start , end])
                        break
                    else:
                        continue
        print(rooms)
        counter = 0
        for room in rooms:
            if len(room) > 0:
                counter += 1
        return counter


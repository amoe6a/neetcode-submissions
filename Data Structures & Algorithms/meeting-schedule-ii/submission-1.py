"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda i : i.start)

        rooms = []
        rooms.append([intervals[0]])
        cur_room_index = 0
        for i in range(1, len(intervals)):
            while intervals[i].start < rooms[cur_room_index][-1].end:
                cur_room_index += 1
                if len(rooms) <= cur_room_index:
                    rooms.append([])
                    break
            rooms[cur_room_index].append(intervals[i])
            cur_room_index = 0
        return len(rooms)
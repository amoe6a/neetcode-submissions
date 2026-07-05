"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        hq = []
        for i in intervals:
            heapq.heappush(hq, (float(i.start), 0))
            heapq.heappush(hq, (float(i.end)-0.1, 1))
        n = heapq.heappop(hq)
        last = None
        while hq:
            if n[1] != last:
                last = n[1]
                n = heapq.heappop(hq)
                
            else:
                return False
        
        return True
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # check ending time and other start time whether they have conflicts
        intervals.sort(key=lambda x:x.start)
        if len(intervals) == 0 :
            return 0
        ends = [intervals[0].end]
        for i in range(1, len(intervals)):
            if intervals[i].start < ends[0]:
                # new meeting starts before the earliest ending meeting ends
                # it need new room
                heapq.heappush(ends, intervals[i].end)
            else:
                heapq.heappop(ends)
                heapq.heappush(ends, intervals[i].end)
        return len(ends)
        
        
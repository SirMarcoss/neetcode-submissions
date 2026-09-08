"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for current in intervals:
            if min_heap and min_heap[0] <= current.start:
                heapq.heappushpop(min_heap, current.end)
            else:
                heapq.heappush(min_heap, current.end)
        
        return len(min_heap)

        



        
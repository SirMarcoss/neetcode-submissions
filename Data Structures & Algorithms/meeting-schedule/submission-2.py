"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start) # start sort --> O(NlogN)
        if not intervals:
            return True

        stack = [intervals[0]]

        for current in intervals[1:]:
            last = stack[-1] # LIFO
            if last.end > current.start:
                return False
            else:
                stack.append(current)
        return True




            






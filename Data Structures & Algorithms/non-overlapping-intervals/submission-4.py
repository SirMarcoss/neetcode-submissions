class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        intervals.sort(key=lambda x: x[0])
        res = 0
        stack = [intervals[0]]

        for current in intervals[1:]:
            last = stack[-1]
            if last[1] > current[0]:
                if last[1] > current[1]:
                    intervals.remove(last)
                    stack.append(current)
                else:
                    intervals.remove(current)
                res += 1
            else:
                stack.append(current)
        return res




        
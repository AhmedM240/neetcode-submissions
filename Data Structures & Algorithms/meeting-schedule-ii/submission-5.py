"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)

        count, res = 0, 0

        start_p, end_p = 0, 0


        while start_p < len(starts):
            if starts[start_p] < ends[end_p]:
                count += 1
                start_p += 1
            else:
                count -= 1
                end_p += 1
            res = max(res, count)
        return res
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

        # sorted?
        intervals.sort(key=lambda x: x.start)
        # printf({lambda x: x.start},{lambda x: x.end})

        prev_end = 0

        for interval in intervals: # i don't think will work?
            if prev_end > interval.start:
                return False
            prev_end = interval.end

        return True




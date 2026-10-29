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
        intervals.sort(key=lambda time: time.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)

        res = 1

        for interval in intervals[1:]:
            if interval.start < heap[0]:
                heapq.heappush(heap, interval.end)
            else:
                while heap and interval.start >= heap[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval.end)

            res = max(res, len(heap))

        return res



class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        heap = []
        intervals.sort(key=lambda x: x.start)

        heapq.heappush(heap, intervals[0].end)

        res = 1

        for meeting in intervals[1:]:

            # Reuse a room if the earliest meeting has ended
            if heap[0] <= meeting.start:
                heapq.heappop(heap)

            # Current meeting now occupies a room
            heapq.heappush(heap, meeting.end)

            res = max(res, len(heap))

        return res
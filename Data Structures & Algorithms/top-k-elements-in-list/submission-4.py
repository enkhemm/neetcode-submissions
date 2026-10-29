class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap = defaultdict(int)
        for n in nums:
            countMap[n] += 1

        heap = []

        for n, count in countMap.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, n))

            # heap is k length and need to check if n should be inserted or not
            if heap[0] < (count, n):
                heapq.heappop(heap)
                heapq.heappush(heap, (count, n))

        return [n for c, n in heap]


# {
#     1: 1,
#     2: 2,
#     3: 3,
#     4: 4
# }

# k = 3, heap = 1, 2, 3, 4
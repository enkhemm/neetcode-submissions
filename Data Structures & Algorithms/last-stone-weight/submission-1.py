class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0
        if len(stones) == 1:
            return stone[0]

        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            x = - heapq.heappop(stones)
            y = - heapq.heappop(stones)

            if x == y:
                continue
            else:
                heapq.heappush(stones, abs(x-y))

        res = stones[0]

        return res
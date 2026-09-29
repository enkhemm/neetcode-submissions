class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        

        # count exact freq using hashmap
        # using values find the highest key, so do k times
        # O( n* )

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # for i in range(k):
        #     most = max(count, key=count.get)
        #     ans.append(most)
        #     popped = count.pop(most)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, [count[num], num])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])


        return res

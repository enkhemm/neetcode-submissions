class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums # why can't we just heapify nums itself?
        self.k = k  # is the constructor the only place where mamber variables can initialized

        heapq.heapify(self.heap)
        while k < len(self.heap):
            heapq.heappop(self.heap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]






        

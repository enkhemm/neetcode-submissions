class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []

        # count exact freq using hashmap
        # using values find the highest key, so do k times

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for i in range(k):
            most = max(count, key=count.get)
            ans.append(most)
            popped = count.pop(most)

        return ans

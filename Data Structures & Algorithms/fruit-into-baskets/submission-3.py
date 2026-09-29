class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # l, r = 0, 1
        # maxLen = 0

        # if len(fruits) == 1:
        #     return 1
        # seen = set((fruits[l], fruits[r]))
        
        # #edge c: if fruits has 1 element
        # for r in range(2, len(fruits)):
        #     if len(seen) < 2 and fruits[r] not in seen:
        #         seen.add(fruits[r])

        #     if fruits[r] not in seen:
        #         maxLen = max(maxLen, r-l+1) # or it's actually r-l+1..
        #         l = r
        #         #update set
        #         seen.clear()
        #         seen.add(fruits[l])

        # maxLen = r-l+1
        # return maxLen

        # above solution no work because we are throwing away the entire prev subarray..

        # brute force:

        # res = 0

        # for l in range(len(fruits)):
        #     types = set()
            
        #     for r in range(l, len(fruits)):
        #         types.add(fruits[r])

        #         if len(types) > 2:
        #             break
        #         res = max(res, r-l+1)

        # return res

        # sliding window

        counts = defaultdict(int)
        l, res = 0, 0 

        for r in range(l, len(fruits)):
            counts[fruits[r]] += 1
            # update when 3 types
            while len(counts) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                l += 1
                

            res = max(res, r-l+1)

        return res









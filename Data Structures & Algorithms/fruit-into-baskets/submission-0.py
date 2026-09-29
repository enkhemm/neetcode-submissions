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

        types = set()
        res = 0

        for l in range(len(fruits)):
            types.add(fruits[l])
            
            for r in range(l+1, len(fruits)):
                if len(types) < 2 and fruits[r] not in types:
                    types.add(fruits[r])
                if fruits[r] not in types:
                    res = max(res, r-l)
                    types.clear()
                    break


        return res










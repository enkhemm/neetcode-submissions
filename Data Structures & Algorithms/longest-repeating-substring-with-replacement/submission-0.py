class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 # left pointer
        replaceCount = k # kth times
        res = 0 # biggest window
        h = {}
        
        for r in range(0, len(s)): # iterating r = 1
            h[s[r]] = h.get(s[r], 0) + 1
            # replaceCount = k - max(h.values()) 
            replaceCount = (r - l + 1) - max(h.values()) # compare ts to k

            while replaceCount > k:
                l += 1
                h[s[l]] = max(0, h[s[l]] - 1)
                replaceCount = (r - l + 1) - max(h.values()) # compare ts to k
            
            res = max(res, r - l + 1) 

            # while replaceCount <= 0:


            # if used up all ks
            # if replaceCount <= k:
            #     h[s[l]] -= -1
            #     l += 1
            # else:
            #     

        return res









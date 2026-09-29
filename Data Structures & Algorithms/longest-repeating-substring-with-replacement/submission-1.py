class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        replaceCount = k 
        res = 0 
        h = {}
    
        """
        {
            A: 1
            B: 1
        }
        """
        # replacementCount: (1 - 0 + 1), 2 - 1

        for r in range(0, len(s)): # iterating r = 1
            h[s[r]] = h.get(s[r], 0) + 1
            replaceCount = (r - l + 1) - max(h.values()) # compare ts to k

            while replaceCount > k:
                
                h[s[l]] = max(0, h[s[l]] - 1)
                l += 1
                replaceCount = (r - l + 1) - max(h.values()) # compare ts to k
            
            res = max(res, r - l + 1) 

        return res









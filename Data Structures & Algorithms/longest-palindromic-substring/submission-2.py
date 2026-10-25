class Solution:
    def longestPalindrome(self, s: str) -> str:
         
        res = ""
        def isPal (l, r):
            nonlocal res
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(res):
                        res = s[l:r+1]
                    
                    l -= 1
                    r += 1

                else:
                    break


        for i in range(len(s) - 1):
            #odd

            isPal(i, i)
            # even
            isPal(i, i+1)

        return res
        
        # ababc
        # acca
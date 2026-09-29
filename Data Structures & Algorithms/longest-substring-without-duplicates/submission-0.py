class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # longest = 0
        # l = 0
        # r = 1
        
        # while r < len(s):
        #     if s[l] == s[r]:
        #         longest = max(longest, len(s[l:r]))
        #         print(s[l:r])
        #         l = r
        #         r = r + 1
        #     r += 1

        # return longest


        longest = 0
        l, r = 0, 1
        seen = set()
        seen.add(s[0])

        so = "abcd"
        print(so[0:1])
        
        while r < len(s):
            if s[r] in seen: # duplicate
                
                # update
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1

            longest = max(longest, len(s[l:r+1]))
            seen.add(s[r])
            r += 1
            

        return longest



        # longest = 0
        # l, r = 0, 1
        # seen = set()

        # while r < len(s):
        #     if s[r] in seen:
        #         longest = max(longest, len(s[l:r]))
        #         l = r
        #         r += 1
        #         seen = set()
        #     else:
        #         seen.add(s[r])
        #         r += 1

        # return longest


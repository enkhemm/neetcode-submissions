class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        iterate through every element in s -- that will be the center of the palindrome
        aabaaaccaaa
        brute force:
        iterate each element in s extend right wondow and check whther pal with helper
        need to also check right part

        another for loop start from end to start
        call is pali and replace curr

        isPali(start, end) -- use 2 ptr approach


        """
        # aca  acca
        def isPal(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True


        longest = ""
        for l in range(len(s)):
            for r in range(l, len(s)):
                if isPal(l, r):
                    if len(s[l:r+1]) > len(longest):
                        longest = s[l:r+1]
                    # longest = max(len(longest), len(s[l:r + 1]))


        for r in range(len(s) - 1, -1, -1):
            for l in range(r, -1, -1):
                if isPal(l, r):
                    if len(s[l:r+1]) > len(longest):
                        longest = s[l:r+1]
                    # longest = max(len(longest, len(s[l:r + 1])))


        return longest

    # ababd
    # lr


    





        
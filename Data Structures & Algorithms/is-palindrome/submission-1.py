class Solution:
    def isPalindrome(self, s: str) -> bool:

        # left, right, i = 0, 1, 0

        # while left is not right:
        #     left += i
        #     right = len(s) - 1 - i - right
        #     if s[left] == " ":
        #         left += 1
        #         continue
        #     if s[right] == " ":
        #         right -= 1
        #         continue
        #     if s[left] != s[right]:
        #         return False
        #     i += 1
        # return True


        newS = []
        for c in s:
            if c.isalnum():
                newS += c.lower()

        return newS == reverse(newS)


        
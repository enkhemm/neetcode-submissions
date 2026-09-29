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


        # newS = []
        # for c in s:
        #     if c.isalnum():
        #         newS += c.lower()
        # # print(newS)

        # # rr = reversed(newS)
        # # print(rr)

        # return newS == newS[::-1]


        # two pointer attempt again:
        left, right, i = 0, len(s) - 1, 0
        l, r = 0, 0

        while left != right:

            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -=1
                continue
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True




        
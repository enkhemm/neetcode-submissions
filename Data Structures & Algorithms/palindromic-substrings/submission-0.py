class Solution:
    def countSubstrings(self, s: str) -> int:
        

        # start, num = 0, 0

        # for end in range(len(s)):
        #     l = start
        #     r = end

        #     while l < r:
        #         # case not palindrome:
        #         if s[l] != s[r]:
        #             #update
        #             if start == 0:
        #                 start += 1
        #             else:
        #                 start -= 1
        #             break
                
        #         l += 1
        #         r -= 1
        #         # if palindrome and end of substring
        #         # if not l < r and s[l] == s[r]:
        #         #     num += 1

        #     if s[l] == s[r]:
        #         num += 1

        # num += len(s)
        # return num


        count = 0

        for start in range(len(s)):
            for end in range(start, len(s)):
                l = start
                r = end
                is_palindrome = True

                while l < r:
                    if s[l] != s[r]:
                        is_palindrome = False
                        break

                    l += 1
                    r -= 1

                if is_palindrome:
                    count += 1

        return count

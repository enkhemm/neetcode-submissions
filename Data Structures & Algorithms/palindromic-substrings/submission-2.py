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


        # count = 0

        # for start in range(len(s)):
        #     for end in range(start, len(s)):
        #         l = start
        #         r = end
        #         is_palindrome = True

        #         while l < r:
        #             if s[l] != s[r]:
        #                 is_palindrome = False
        #                 break

        #             l += 1
        #             r -= 1

        #         if is_palindrome:
        #             count += 1

        # return count


    #     l, r = 0, 0
    #     count = 0
    #     for i in range(len(s)):
    #         # out of bounds:

    # whi
    #         isPalin = True

    #         if l < 0 or r > len(s)-1:
    #             l, r = i, i
    #             break

    #         if s[l] != s[r]:
    #             isPalin = False

    #         if isPalin:
    #             count += 1
            
    #         l = i - 1
    #         r = i + 1


    #     # even portion
    #     for i in range(len(s)):
    #         # out of bounds:


    #         l, r = i, i + 1
    #         isPalin = True

    #         if l < 0 or r > len(s)-1:
    #             break

    #         if s[l] != s[r]:
    #             isPalin = False

    #         if isPalin:
    #             count+=1
            
    #         l -= 1
    #         r = l + 1

    #     return count



        count = 0
        for i in range(len(s)):
            l=r=i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count








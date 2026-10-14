class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # res = [0] * len(temperatures)

        # for i in range(len(temperatures)):
        #     counter = 1
        #     for j in range(i + 1, len(temperatures)):

        #         if temperatures[j] > temperatures[i]:
        #             res[i] = counter
        #             break
        #         else:
        #             counter += 1


        # return res
                                    # i    j          
    # temperatures = [30,38,30,36,35,34,28]
    # stack = [   ]

        res = [0] * len(temperatures)
        stack = []
    # stack = [30-0, ]

    # curr = 38-1

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                res[stack[-1][1]] = i - stack[-1][1] 
                stack.pop(-1)

            stack.append((t, i))

        return res

        
        # AI example..
        n = len(temperatures)
        res = [0] * n

        # Iterate backwards from second to last element
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    # No warmer day exists past j, so none exists for i
                    j = n
                    break
                # Leapfrog directly to the next candidate
                j += res[j]

            if j < n:
                res[i] = j - i

        return res


        
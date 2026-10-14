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




        
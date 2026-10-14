class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            counter = 1
            for j in range(i + 1, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    res[i] = counter
                    break
                else:
                    counter += 1


        return res
                                    # i    j          
    # temperatures = [30,38,30,36,35,34,28]
    # counter = 1
    # [1, 4    ]
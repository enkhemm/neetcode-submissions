class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # sorted1 = "".join(sorted(s1))
        # sorted2 = "".join(sorted(s2))
        # print


        # for i in range(len(sorted1)):
        #     if sorted1[i] != sorted2[i]:
        #         return False

        # return True 

        # second try
        # check = set(s1)
        
        # for i in range(len(s2)):
        #     while s2[i] not in check:
        #         continue
        #     i
            

        # return True


        sorted1 = "".join(sorted(s1))
        length = len(sorted1)

        for i in range(len(s2) - length + 1):
            window = "".join(sorted(s2[i:i+length]))
            #print(window)
            if sorted1 == window:
                return True

        return False

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     count1 = {}
    #     for c in s1:
    #         count1[c] = 1 + count1.get(c, 0)

    #     need = len(count1)
    #     for i in range(len(s2)):
    #         count2, cur = {}, 0
    #         for j in range(i, len(s2)):
    #             count2[s2[j]] = 1 + count2.get(s2[j], 0)
    #             if count1.get(s2[j], 0) < count2[s2[j]]:
    #                 break
    #             if count1.get(s2[j], 0) == count2[s2[j]]:
    #                 cur += 1
    #             if cur == need:
    #                 return True
    #     return False



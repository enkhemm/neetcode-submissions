class Solution:
    #def checkInclusion(self, s1: str, s2: str) -> bool:

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

        def checkInclusion(self, s1: str, s2: str) -> bool:
        
            s1 = sorted(s1)

            for i in range(len(s2)):
                for j in range(i, len(s2)):
                    subStr = s2[i : j + 1]
                    subStr = sorted(subStr)
                    if subStr == s1:
                        return True
            return False






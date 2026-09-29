class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sorted1 = "".join(sorted(s1))
        sorted2 = "".join(sorted(s2))


        for i in range(len(sorted1)):
            if sorted1[i] != sorted2[i]:
                return False

        return True 
        
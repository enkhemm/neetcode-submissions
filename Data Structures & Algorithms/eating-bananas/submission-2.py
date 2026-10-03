class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.sort()
        # k = 1
        # m = max(piles) # max value

        # for _ in range(m):
        #     good_k = True
        #     time = 0
        #     for i in range(len(piles)):
        #         time += (piles[i] + k - 1) // k #k math.ceil(piles[i]/k)
        #         if time > h:
        #             good_k = False
        #             break
                                
        #     if not good_k:
        #         k += 1
        #     else:
        #         break


        # return k

    # piles = [1,2,3,4], h = 9
    # k = 1
    # m = 4
    # good_k = T

    # for.. time = 10 


    # AFTER SOLUTION

    # class Solution:
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)

            if totalTime <= h:
                return speed
            speed += 1
        return speed



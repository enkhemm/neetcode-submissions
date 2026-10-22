class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # start from reverse index
        #     curr += i if it;s bigger than we i -- if not continue to add from here until curr > amount
        #     test first and then add
        #     if bigger up until the zeroth
        #     curr = amount return count

        # return -1

        curr = 0
        count = 0

        for i in range(len(coins) - 1, -1, -1):
            while curr + coins[i] <= amount:
                curr += coins[i]
                count += 1
            if curr == amount:
                return count
            # else: # if adding coint overshoots the amount:
            #     continue

        return -1

        # [1,5,10]

        # i = 0
        # count = 3
        # curr = 12
            

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # My optimized implementation
        # range of the BS is the capacity itself the anwer
        l = max(weights)
        r = sum(weights)

        def isValid(cap) -> bool:
            curr_days = 1
            total = 0

            for w in weights:
                if total + w > cap:                    
                    curr_days += 1
                    if curr_days > days:
                        return False
                    total = w
                else:
                    total += w

            return True


        
        while l < r:
            m = (l+r) // 2 # ceiling division? floor division??
            if isValid(m):
                r = m
            else:
                l = m + 1

        return r
#                      i        
# weights = [1,5,4,4,2,3], days = 3
# \
# l = 8  r = 8
# m = 7
# isValid(7): - false
# total = 2
# c_d = 3








        # After looking at solution
        # curr = max(weights)
        

        # while True:
        #     total = 0
        #     curr_days = 1
        #     for w in weights:
        #         if total + w > curr:
        #             total = w
        #             curr_days += 1
        #         else:
        #             total += w

        #     if curr_days > days:
        #         curr += 1
        #     else:
        #         return curr
        
# weights = [1,5,4,4,2,3], days = 3

# curr = 5
# c_d =  1
# total = 5

        # My approach first..
        # curr = max(weights) # first capacity
        # curr_days = 0

        # while True:
        #     i = 0
        #     total = 0
        #     while i <= len(weights) - 1:
        #         if total + weights[i] > curr:
        #             total = 0
        #             curr_days += 1
        #             continue
        #         else:
        #             total += weights[i]
        #         i += 1
           
        #     if curr_days > days:
        #         curr += 1
        #     else:
        #         break
            
        # return curr


        



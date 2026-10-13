class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        curr = max(weights) # first capacity
        curr_days = 0

        while True:
            i = 0
            total = 0
            while i <= len(weights) - 1:
                if total + weights[i] > curr:
                    total = 0
                    curr_days += 1
                    continue
                else:
                    total += weights[i]
                i += 1
           
            if curr_days > days:
                curr += 1
            else:
                break
            
        return curr
# weights = [1,5,4,4,2,3], days = 3

# curr = 5
# c_d =  1
# i = 2,  total = 0
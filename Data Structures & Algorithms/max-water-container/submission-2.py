class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0
        curr = 0
        # iterate thru array using a, i in enumerate(nums):
        # we could try peaking into the r-1 and l+1 and update to the one that is bigger

        l = 0
        r = len(heights) - 1

        # while r - l >= 1:
        while r > l:
            curr = min(heights[l], heights[r]) * (r - l)
            if curr > maxArea:
                maxArea = curr
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


            
            # update
            # if heights[r - 1] > heights[l + 1]:
            #     r -= 1
            # elif heights[r - 1] < heights[l + 1]:
            #     l += 1
            # # the same
            # else:
            #     if heights[r] > heights[l]:
            #         l += 1
            #     if heights[r] < heights[l]:
            #         r -= 1
            #     else:
            #         l += 1

        return maxArea
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #
        # start at middle
        # if target less go to left middle
        # if target more go to right middle
        # if found return index

        # return -1

        # # using resursion not work bcz only need index

        # midInd = len(nums) // 2

        # # target = 1, [-1,0,2,4,6,8]
        # # mid = 3 -> 1 -> 1//2 = 

        # while True
        # if nums[midInd] == target:
        #     return midInd
        # if :
        #     return -1
        # elif nums[midInd] < target:
        #     midInd = midInd // 2 #3//2 = 1
        # elif nums[midInd] > target:
        #     midInd = (midInd // 2) + midInd 

        # return -1

        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else: #found:
                return mid

        return -1
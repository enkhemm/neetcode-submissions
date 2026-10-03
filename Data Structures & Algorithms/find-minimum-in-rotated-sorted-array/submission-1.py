class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 0
        """
        l,r

        while l <= r:
            mid = (l+r) // 2
            # go to left if left > mid

            # else the split occured on right
        """

        l, r = 0, len(nums) - 1


        while l <= r:
            mid = (l+r) // 2

            if nums[l] < nums[mid] and nums[mid] < nums[r]:
                return nums[0]

            if nums[l] > nums[mid]:
                r = mid - 1

            # go to side that is unsorted
            else:
                l = mid + 1

        return min(nums[r], nums[l])

        


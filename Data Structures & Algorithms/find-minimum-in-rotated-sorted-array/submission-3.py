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

        while l < r:
            mid = (l+r) // 2

            # 4 5  6 1 2
            if nums[mid] > nums[r]:
                l = mid + 1

            # 6 1 2 4 5
            else:
                r = mid

        return nums[l]

        


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid

        


            if nums[m] > target:
                if nums[l] > nums[r]:
                    l = m + 1
                else:
                    r = m-1
            else: 
                if nums[l] > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


        # [6,5,4,3,2,1]  t = 5
        # l = 0
        # r = 5
        # m = 2 [4]
        # if [m] > t:
        #     if [l] > [r]:
        #         l = m + 1
        #     else:
        #         r = m-1
        # else: 
        #     if [l] > [r]:
        #         r = m - 1
        #     else:
        #         l = m + 1




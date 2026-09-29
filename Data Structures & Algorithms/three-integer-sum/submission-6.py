class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i, a in enumerate(nums):
            if i != 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum == 0:
                #else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        
        return res









        for i in range(len(nums) - 1):

            if i != 0 and nums[i] == nums[i-1]: #duplicate
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
            
            i += 1

        return res


        


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = set()

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
#                         result.add(triplet)

#         return [list(triplet) for triplet in result]
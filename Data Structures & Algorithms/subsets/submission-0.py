class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(index, path):
            if index >= len(nums):
                res.append(path.copy())
                return

            # case 1: to include element at ind
            path.append(nums[index])
            backtrack(index+1, path)

            # case 2: not include the element at ind
            path.pop()
            backtrack(index + 1, path)

        backtrack(0, [])

        return res

        
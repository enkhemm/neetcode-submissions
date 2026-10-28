class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        num2ind = {}
        for i, n in enumerate(nums):
            if n not in num2ind:
                num2ind[n] = i
            else:
                if abs(num2ind[n] - i) <= k:
                    return True
                else:
                    num2ind[n] = i

        return False

        
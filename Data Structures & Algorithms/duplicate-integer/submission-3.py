class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_n = sorted(nums)
        for i in range(len(sorted_n)):
            for j in range(i+1, len(sorted_n)):
                if sorted_n[i] == sorted_n[j]:
                    return True
        return False

        
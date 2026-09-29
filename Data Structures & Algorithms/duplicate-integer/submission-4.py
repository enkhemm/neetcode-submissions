class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_n = sorted(nums)
        for i in range(len(sorted_n) - 1):
            if sorted_n[i] == sorted_n[i+1]:
                return True
            
        return False

        
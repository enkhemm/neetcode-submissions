class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        check if len 1 return 1
        temp = 0
        repeat k times -- while
        1,2,3,4
        temp = 4
        4-> 3
        3 -> 2
        2 -> 1

        4123

        for i start from 1 until len

            store last element in temp

            a[i] = a[i-1]
        a[0] = temp
        k--
        """

        while k != 0:
            temp = nums[len(nums) - 1]
            for i in range(len(nums)-1, 0, -1):
                
                nums[i] = nums[i-1]
            nums[0] = temp    
            k -= 1
    
                
                



        
        
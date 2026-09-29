# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:

#         l = 0
#         r = l + 1

#         while True: 
#             toFind = target - numbers[l]

#             while  numbers[r] <= toFind:
#                 if numbers[r] == toFind:
#                     return [l + 1, r + 1]
#                 elif r == len(numbers) - 1:
#                     break
                
#                 r += 1

#             l += 1
#             r = l + 1


#         return []

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        currSum = numbers[l] + numbers[r]

        while currSum != target:
            if currSum > target:
                r -= 1
            if currSum < target:
                l += 1

            currSum = numbers[l] + numbers[r]


        return [l+1, r+1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = l + 1

        while True: 
            toFind = target - numbers[l]

            while  numbers[r] <= toFind:
                if numbers[r] == toFind:
                    return [l + 1, r + 1]
                elif numbers[r] == len(numbers) - 1:
                    break
                
                r += 1

            l += 1
            r = l + 1


        return []


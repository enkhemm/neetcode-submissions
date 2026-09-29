class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # if (len(numbers) < 2)

        r = 0
        l = r + 1

        while True: 
            toFind = target - numbers[r]

            while numbers[l] <= toFind:
                if numbers[l] == toFind:
                    return [r + 1, l + 1]
                
                l += 1

            r += 1
            l = r + 1


        return []


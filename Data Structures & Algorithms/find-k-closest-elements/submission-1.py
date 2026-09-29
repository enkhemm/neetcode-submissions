class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        res =[]
        l = 0

        for r in range(len(arr)):
            # keep adding to list until len = k
            if len(res) != k:
                res.append(arr[r])
                continue

            # case to add to res
            if abs(arr[r] - x) == abs(arr[l] - x):
                continue
                
                #break

            # while arr[r] == arr[r+1]:
            #     continue
            if abs(arr[r] - x) < abs(arr[l] - x):
                del res[0]
                res.append(arr[r])
                l +=1
            

        return res

        
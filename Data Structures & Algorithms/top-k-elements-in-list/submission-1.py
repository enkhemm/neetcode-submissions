class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        print(counts)

        #uns_list = [len(counts)]??
        
        uns_list = []
        for key, count in counts.items():
            # populate uns_list so that count is 0th and key is 1st
            # for i in range(len(counts) - 1):
            #     uns_list[i] = [count, key]
            #     map(counts.get()[0])

            uns_list.append(list([count, key]))

        print(uns_list)
        #sort the uns_list so that highest counts go to the end
        # 
        s_list = sorted(uns_list)

        answer = []
        for i in range(k):
            element = s_list.pop()
            answer.append(element[1])

        return answer
            
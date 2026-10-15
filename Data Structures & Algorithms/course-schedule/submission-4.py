class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # recursive dfs.. kahn??
        """
        crsMap =  prereq:  [all the courses]
        indegree = [] -> ith element is the ith course: say how many  prereq are required to take the course
        prereq can be taked if it has indegree 0

        process all the prereqs and so on..
        def helper(crs) -> :
            crs enters a q
            while p
            pop
            find all courses required by this crs
            decrement their indegrees..
            if their indegree == 0
            enter a q


        for crs in map:
            if indgree[crs] == 0
                helper(crs)

        
        """

        #          3
        #     1    2    
        # 0              4




        # [[0,1],[1,2], [2, 4], [1, 3]]

        # preMap =  0: 1   1: 2, 3    2: 4 
        

        # preMap =    1: 0      2: 1      4: 2    3:  1
        indeg = [1, 2, 1, 0, 0]


        preMap = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            indegree[crs] += 1

        q = deque()
        count = 0

        for crs in preMap:
            if indegree[crs] == 0:
                q.append(crs)
                

        while q:
            crs = q.popleft()
            count += 1
            for dependent in preMap[crs]: # get every class who depends on crs
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)

        return count == numCourses




        
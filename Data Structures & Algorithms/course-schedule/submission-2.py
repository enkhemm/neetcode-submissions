class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        solve using kahn's algo topologivca l sort:
        import collections
        """

        # prereq  = [[0, 1], [1, 2], [2, 3]] [4] 
        indegree = [0] * numCourses # for each course, number of prereqs
        adj = defaultdict(list) # for each prereq, what course depended on it
        completed = 0

        # fill the adj list:
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        # filling out the queue and completed
        q = deque() # all the courses that can be taken cz prereq satisfied
        for i, crs in enumerate(indegree):
            if crs == 0:
                completed += 1
                q.append(i)

        while q:
            crs = q.popleft()
            for dependent in adj[crs]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    completed += 1
                    q.append(dependent)

        
        return completed == numCourses


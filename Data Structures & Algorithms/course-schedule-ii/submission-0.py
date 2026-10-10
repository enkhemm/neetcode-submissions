class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        """
        indegree = 0 * numCourses, adj: prer -> [courses]
        res # the orders in which to take classes

        obs: length result has to be the same as numCourses otherwise return []
        q has crs that have no prereq
        while q
        pop q -> append to list


        """

        indegree = [0] * numCourses # how many prereqs for this course
        res = []
        adj = defaultdict(list)

        # populate the adj pre -> list of courses that depend on it and indegree
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque()
        for i, crs in enumerate(indegree):
            if crs == 0:
                q.append(i)

        while q:
            crs = q.popleft()  # extracting course with no prereps can take it
            res.append(crs)
            for dependent in adj[crs]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)

        
        return res if len(res) == numCourses else []

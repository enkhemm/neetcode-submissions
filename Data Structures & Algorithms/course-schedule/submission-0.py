class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        why are we even given the numcourses variable? cant we just determine it on our own by counting all the unique numbers in the list?
        (would use a set)

        topological sort?
        we find the courses that dont have any dependencies and then increment some coursees taken var
        but also of each pair in the list we go as deep as we can to mao out which courses are dependent on it
        almost like backtracking??

        and we can use a hashmap and also keep track of all the elements we foudn in a set because if there is a cycle we 
        need to understand maps!!
        
        """
        preMap = defaultdict(list) #would defaultdict even work in this case
        # preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        count = 0

        def dfs(crs):

            
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            preMap[crs] = []

            return True

        for c in range(numCourses):

            if not dfs(c):
                return False

        return True















        
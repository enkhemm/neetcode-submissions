class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        vt: no cycles, all the nodes are conntected, set for pathways, set validsubtree
        n == endges - 1  -- not a good determinant
        how to check wither a subtree that is valid is part of a tree that is already there, that they are all connected
        ds: 

        build map parent - list of choildren 


        dfs(node, path):

            if node is set: false
            if node has  no children return true

            for every child:
                dfs

                after popping out remove from the path
                add it to valid tree set


        go thru every parent in the map and dfs:
            if this is a node connection taht doesnt tie to our main  tree then false : not a connected node 
                false

        return true


        """

        treeMap = defaultdict(list)
        path = set()


        for parent, child in edges:
            treeMap[parent].append(child)


        def dfs(node) -> bool:
            if node in path: return False

            if treeMap[node] == []: return True

            # this node is nto cyclic, and has children
            path.add(node)

            for child in treeMap[node]:
                if not dfs(child):
                    return False

                path.remove(child)

        

        for parent in treeMap:
            if dfs(parent) == False:
                return False
            if parent not in validSubtree: # the node is connected
                return False


        return True
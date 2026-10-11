class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        vt: no cycles, all the nodes are conntected, set for pathways, set validsubtree
        n == endges - 1
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

        return True if n == (len(edges) + 1) else False
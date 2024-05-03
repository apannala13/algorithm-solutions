class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #parent array where par[i] is parent of node i 
        #each node is its own parent at the start to represent self loop
        par = [i for i in range(len(edges) + 1)] 

        #rank array used to keep the track of the depth of the tree
        rank = [1] * (len(edges) + 1)

        #find the representative (root) of the set containing n
        def find(n):
            #start with node n itself
            p = par[n]
            #find root of the set. root node is the one whos parent is itself
            while p != par[p]:
                #path compression: point the current node directly to its grandparent,
                #shortening the path from all nodes directly
                par[p] = par[par[p]]
                #move to parent node, now two levels up
                p = par[p]
            return p #return root node of set which contains n 

        #union function to merge the sets containing nodes n1 and n2
        def union(n1, n2):
            #find roots of the nodes n1 and n2
            p1, p2 = find(n1), find(n2)
            #if roots are same, adding this edge forms a cycle
            if p1 == p2:
                return False 
            #union by rank: attach smaller tree under larger tree
            if rank[p1] > rank[p2]:
                par[p2] = p1 #make root of n1 the new root
                rank[p1] += rank[p2] #update rank of new root
            else:
                par[p1] = p2 
                rank[p2] += rank[p1]
            return True 

        for n1, n2 in edges:
            if not union(n1, n2): #try to union nodes, if returns False, theres a cycle
                return [n1, n2] #return edge causing cycle

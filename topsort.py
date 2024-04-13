"""
Given a directed graph G(V,A), we want to order the vertices according
to a rank function r in such a way that for every arc (u,v), we have r(u) < r(v)

e.g: input: 1 -> 2, 1 -> 5, 3 -> 1, 5 -> 2, 5 -> 4
     output: 3 -> 1 -> 5 -> 4, 1 -> 2, 5 -> 2

linear time in size of input 

"""

from collections import defaultdict, deque 

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) #graph with number of vertices
        self.V = vertices #total num of vertices in graph

    def add_edge(self, u, v):
        self.graph[u].append(v) #directed edge from vertex u to vertux v

    def top_sort_util(self, v, visited, stack):
        #helper for dfs traversal
        visited[v] = True #mark current node as visited

        #Recurse for all vertices adjacent to vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.top_sort(i, visited, stack)
        #push current vertex to stack to store result
        stack.append(v)

    def top_sort(self):
        visited = [False] * self.V #mark all vertices as not visited
        stack = [] #stack to store result

        #recurse to store top sort from all vertices, one by one
        for i in range(self.V): 
            if not visited[i]:
                self.top_sort_util(i, visited, stack)

        return stack[::-1] #return elements in reverse order 

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(4, 1)

    print(g.top_sort())
    




"""
UnionFind algorithm, on a disjoint set data structure (non-overlapping sets).
Finds the root parent of an element, and determines whether two elements 
are in same set. 
If two elements are in different sets, merge the smaller set to larget set.
Connected components => graph
"""

class UnionFind:
    def __init__(self, size: int):
        # Initialize each element to be its own parent, forming 'size' disjoint sets.
        self.parent = list(range(size))
        # Initialize the height of each tree as 0, since they are all individual elements.
        self.height = [0] * size

    def find(self, element):
        # Recursively find the top-most parent (leader) of an element.
        # Path compression: make the found representative the direct parent of the element
        # to optimize future searches.
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1: int, element2: int):
        # Connects the sets that element1 and element2 belong to.
        # find the leaders of both elements.
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 == root2:
            # If leaders are the same, elements are already in the same set.
            return False

        # Union by height: attach the shorter tree to the root of the taller tree.
        # helps keep the tree as flat as possible.
        if self.height[root1] > self.height[root2]:
            self.parent[root2] = root1
        elif self.height[root1] < self.height[root2]:
            self.parent[root1] = root2
        else:
            # If heights are equal, choose one as the new parent and increment height
            # as this union may increase the tree's height by 1.
            self.parent[root2] = root1
            self.height[root1] += 1
        return True

if __name__ == "__main__":
    u = UnionFind(5)
    # Connect elements 0 and 1 into one set.
    u.union(0, 1)
    # Connect elements 2 and 3 into another set.
    u.union(2, 3)
    # Connect the sets of elements 1 and 2 together, forming a single set for 0, 1, 2, 3.
    print(u.find(0) == u.find(3)) # Check if elements 0 and 3 are in the same set: True.
    print(u.find(0) == u.find(4)) # Check if elements 0 and 4 are in the same set: False.
    assert u.find(0) == u.find(3)
    

    

"""
MinHeap implementation : for any given node C, if P is a parent node of C, 
                         the value of P is less than or equal to value of C.
"""


class Heap:
    def __init__(self, items:int):
        self.heap = [None] #store heap elements
        self.rank = {}  #keep track of elements within heap (unique)
        for x in items: #item inserted into heap
            self.push(x) 

    def __len__(self):
        return len(self.heap) - 1   #account for dummy element

    def push(self, x):
        assert x not in self.rank  #uniqueness check using dict
        i = len(self.heap) 
        self.heap.append(x) #add element to end of heap, as last leaf in tree
        self.rank[x] = i #map items to idx, using length of heap as val and item as key
        self.up(i) #restore heap order: move x up the heap if needed, to ensure minheap properties

        
    def pop(self) -> int:
        root = self.heap[1] #return root (smallest element of heap)
        del self.rank[root] #remove root from items dict
        x = self.heap.pop() #remove last element from heap
        if len(self.heap) > 0: #if heap not empty
            self.heap[1] = x #place last element at root
            self.rank[x] = 1 #update rank
            self.down(1) #restore min-heap property by moving new root down to position
        return root 

    def up(self, i):
        x = self.heap[i] #element to potentially move up to right position
        while i > 1 and x < self.heap[i//2]: #
            self.heap[i] = self.heap[i//2]
            self.rank[self.heap[i//2]] = i 
            i //= 2 
        self.heap[i] = x 
        self.rank[x] = i 

    def down(self, i):
        x = self.heap[i]
        n = len(self.heap)
        while True:
            left = 2 * i
            right = left + 1 
            if (right < n and self.heap[right < x and
                    self.heap[right] < self.heap[left]):
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i 
                i = right 
            elif left < n and self.heap[left] < x:
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i 
                i = left
            else:
                self.heap[i] = x
                self.rank[x] = i 
                return 
    def update(self, old, new):
        i = self.rank[old]
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i 
        if old < new:
            self.down(i)
        else:
            self.up(i)


if __name__ == "__main__":
    h = Heap(4)
    

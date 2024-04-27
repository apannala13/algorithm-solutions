class Node:
    def __init__(self, key, value):
        self.key = key  
        self.value = value  
        self.prev, self.next = None, None  #initialize left(prev) and right(next) links (None)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  #maximum # of items cache can hold
        self.cache = {}  #map keys to node objects
        
        #create left and right boundary nodes that don't hold real data
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right  #left boundary node points to right boundary node
        self.right.prev = self.left  #right boundary node points back to left boundary node
    
    #remove a node from its current position in the list
    def remove(self, node):
        #link the node's left and right neighbors directly to each other, skipping the node
        left_neighbor, right_neighbor = node.prev, node.next  #identify neighbors.
        left_neighbor.next = right_neighbor  #point left node to right node
        right_neighbor.prev = left_neighbor  #point right node to left node
    
    #insert a new node right before the right boundary node
    def insert(self, node):
        #references to the last node in the middle and the right boundary node
        last_middle_node, right_boundary = self.right.prev, self.right
        last_middle_node.next = node #last middle node points to new node
        right_boundary.prev = node #rightmost node points to new node
        #make node also point to rightmost and last middle boundaries
        node.next, node.prev = right_boundary, last_middle_node 
    
    #acess the value of the node with the given key if it exists
    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])  #remove the node from its current position
            self.insert(self.cache[key])  #reinsert the node right before the right boundary
            return self.cache[key].value  #return the node's value
        return -1  #if key not found
    
    # Update or insert a new key-value pair.
    def put(self, key: int, value: int) -> None:
        if key in self.cache:  #if the key already exists,
            self.remove(self.cache[key])  #remove the existing node
        self.cache[key] = Node(key, value)  #create a new node or update existing
        self.insert(self.cache[key])  #insert the new node before the right boundary
        if len(self.cache) > self.capacity:  #evict lru node
            lru = self.left.next  #lru node is right after the left boundary
            self.remove(lru)  #remove the least recently used node from the linked list
            del self.cache[lru.key]  #as well as from the cache dictionary

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)

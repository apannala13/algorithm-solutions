"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        
        node = head
        while node.next != head:
            if node.val <= insertVal <= node.next.val:
                break
            elif node.val > node.next.val:
                if insertVal >= node.val or insertVal <= node.next.val:
                    break
                    
            node = node.next 
            
        
        newNode = Node(insertVal, node.next)
        node.next = newNode
        return head
    
            

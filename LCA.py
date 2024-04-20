# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None 

        cur = root

        while cur:
            #if both nodes p and q are greater than current, move to the right subtree.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right #update cur to root of right subtree
            #if both nodes p and q are less than current, move to left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left #update cur to root of left subtree
          #if a split occurs where p and q are on different sides of cur, following the properties of a BST,
          #then we return cur (the parent node), as they are on different subtrees
            else:
                return cur  #current node is the LCA of p and q
                
        

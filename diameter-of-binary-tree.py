# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = float('-inf')

        def dfs(node):
            nonlocal longest 

            if not node:
                return 0 
                
            #recursively find height of left and right children
            left, right = dfs(node.left), dfs(node.right)
            
            #update the longest diameter. checks if current nodes
            #path (left + right) is the longest path that passes thru current node
            #derived from counting all edges from leftmost left of left subtree
            #to rightmost leaf of right subtree
            #may be longest path in the entire tree even if it does not pass thru root of the enire tree
            longest = max(longest, left + right)

            #return height of tree for current node
            #needed to calculate diameters
            #1 for the current node, plus maximum of heights
            return 1 + max(left, right)

        dfs(root)
        return longest 

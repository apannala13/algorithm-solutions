# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True #flag

        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left) #height of left subtree
            right = dfs(node.right) #height of right subtree

            if abs(left - right) > 1: #binary tree is not balanced
                self.balanced = False

            #calculate and return the height of the current node
            # +1 for the current node itself plus the height of its taller subtree
            return 1 + max(left, right)

        dfs(root)
        return self.balanced 



            

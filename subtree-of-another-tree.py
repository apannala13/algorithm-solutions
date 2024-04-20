# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False #empty tree cannot contain subtree
        if not subRoot:
            return True #empty subtree is technically subtree of ANY tree
        
        def sametree(s, t):
            if not s and not t:
                return True #both can be empty, identical
            if not s or not t:
                return False #one cannot be empty, not identical
            #recursively check that structure of tree and values are the same
            return (s.val == t.val) and sametree(s.left, t.left) and sametree(s.right, t.right)

        def dfs(root, subRoot):
            #if dfs reaches a null node, it returns False for this path, but 
            #recursion continues for other paths.
            #ensures all potential starting points in the tree are checked, 
            #even if some paths reach a dead end
            if not root:
                return False  
            #call helper
            if sametree(root, subRoot):
                return True 
            #recursively traverse left and right to find any subtree match in the main tree
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf') 

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0 
            #recursively calculate max path sums of left and right child
            left, right = dfs(node.left), dfs(node.right)  
            #only take non negative sums to maximize path sum
            leftmax = max(left, 0)
            rightmax = max(right, 0)
            
            #calculate max path sum passing thru current node 
            cur_sum = node.val + leftmax + rightmax 
            max_sum = max(max_sum, cur_sum)
            
            #need to choose the path that contributes most to the sum
            #including the current nodes value
            #passed up the recursion call stack
            return node.val + max(leftmax, rightmax)
        
        dfs(root)
        return max_sum

            

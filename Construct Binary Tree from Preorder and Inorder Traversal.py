# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        
        #first val in preorder list is the root 
        #the values to the left of the root node in the inorder list
        #will always be the left subtree, and the values to the right will 
        #be in the right subtree

        root = TreeNode(preorder[0]) #first val of our treenode will always be first val (root)
        mid = inorder.index(preorder[0]) #find position of root val in inorder list
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) #preorder from index 1 to mid, inorder up till mid 
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root 
        

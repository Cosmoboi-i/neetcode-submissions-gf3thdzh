# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(self, root):
            if root == None:
                return None
            
            root.left, root.right = root.right, root.left

            dfs(self, root.left)
            dfs(self, root.right)
        
        dfs(self, root)
        return root
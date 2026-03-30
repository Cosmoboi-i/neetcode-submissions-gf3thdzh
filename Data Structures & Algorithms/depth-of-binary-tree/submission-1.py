# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        length = 0

        def dfs(root, curLen):
            if not root:
                return 0
            
            return 1 + max(dfs(root.left, curLen + 1), dfs(root.right, curLen + 1))
        
        return dfs(root, 0)

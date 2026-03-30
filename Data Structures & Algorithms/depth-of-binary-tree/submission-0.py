# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        length = 0

        def dfs(self, root, curLen):
            if not root:
                nonlocal length
                length = max(length, curLen)
                return
            
            dfs(self, root.left, curLen + 1)
            dfs(self, root.right, curLen + 1)
        
        dfs(self, root, 0)

        return length
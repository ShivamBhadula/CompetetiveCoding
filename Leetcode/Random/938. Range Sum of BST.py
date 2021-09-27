# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return []
            return dfs(root.left)+[root.val]+dfs(root.right)
        
        sum=0
        tree=dfs(root)
        for i in tree:
            if i >=low and i<=high:
                sum+=i
        
        return sum
        
        
        

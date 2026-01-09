#https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, cur_depth):
            if node is None:
                return -1, None

            if node.left is None and node.right is None:
                return cur_depth, node

            ld, ln = dfs(node.left, cur_depth + 1)
            rd, rn = dfs(node.right, cur_depth + 1)

            if ld == rd:
                return ld, node
            
            if ld > rd:
                return ld, ln
            return rd, rn

        d, node = dfs(root, 0)
        return node
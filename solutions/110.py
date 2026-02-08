#https://leetcode.com/problems/balanced-binary-tree/description/?envType=daily-question&envId=2026-02-08
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node is None:
                return True, 0

            lt, l = solve(node.left)
            rt, r = solve(node.right)
            return abs(l - r) < 2 and lt and rt, max(l, r) + 1

        return solve(root)[0]
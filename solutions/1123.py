#https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/?envType=daily-question&envId=2025-04-04
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        node, depth = self.dfs(root, 0)
        return node


    def dfs(self, node, depth):
        if node == None:
            return (None, depth - 1)

        lnode, ldepth = self.dfs(node.left, depth + 1)
        rnode, rdepth = self.dfs(node.right, depth + 1)

        if ldepth == rdepth:
            return (node, ldepth)
        elif ldepth > rdepth:
            return (lnode, ldepth)
        else:
            return (rnode, rdepth)
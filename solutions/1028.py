#https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/?envType=daily-question&envId=2025-02-22
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        num = ""
        idx = 0
        while idx < len(traversal) and traversal[idx] != "-":
            num += traversal[idx]
            idx += 1 
        
        root = TreeNode(int(num))
        if len(traversal) == 1:
            return root

        
        self.dfs(traversal[idx:], root, 0)
        return root

    def dfs(self, traversal, parent, parent_depth):
        if len(traversal) == 0:
            return ""

        next_depth = 0
        idx = 0
        while traversal[idx] == "-" and idx < len(traversal):
            next_depth += 1
            idx += 1

        if next_depth != parent_depth + 1:
            return traversal

        if idx == len(traversal):
            return ""

        num = ""
        while idx < len(traversal) and traversal[idx] != "-":
            num += traversal[idx]
            idx += 1 
        
        new_node = TreeNode(int(num))
        parent.left = new_node
        if idx == len(traversal):
            return ""
        traversal = self.dfs(traversal[idx:], new_node, next_depth)

        if len(traversal) == 0:
            return ""
        next_depth = 0
        idx = 0
        while traversal[idx] == "-" and idx < len(traversal):
            next_depth += 1
            idx += 1

        if next_depth != parent_depth + 1:
            return traversal

        if idx == len(traversal):
            return ""
        num = ""
        while idx < len(traversal) and traversal[idx] != "-":
            num += traversal[idx]
            idx += 1 
        new_node = TreeNode(int(num))
        parent.right = new_node

        if idx == len(traversal):
            return ""

        return self.dfs(traversal[idx:], new_node, next_depth)

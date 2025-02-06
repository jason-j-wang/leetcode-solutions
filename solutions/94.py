#https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=problem-list-v2&envId=depth-first-search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        if root == None:
            return arr

        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right, arr)

        return arr
        
    def dfs(self, node, arr):
        if node == None:
            return

        self.dfs(node.left, arr)
        arr.append(node.val)
        self.dfs(node.right, arr)
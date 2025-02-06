#https://leetcode.com/problems/validate-binary-search-tree/?envType=problem-list-v2&envId=depth-first-search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bst = []

        if root == None:
            return True

        self.dfs(root.left, bst)
        bst.append(root.val)
        self.dfs(root.right, bst)

        for i in range(1, len(bst)):
            if bst[i] <= bst[i-1]:
                return False
        return True
        

    def dfs(self, node, bst):
        if node == None:
            return

        self.dfs(node.left, bst)
        bst.append(node.val)
        self.dfs(node.right, bst)
        

        
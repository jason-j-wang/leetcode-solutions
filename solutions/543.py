#https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if node == None:
                return 0

            if node.left == None and node.right == None:
                return 1

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            nonlocal ans
            ans = max(ans, left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        dfs(root)

        return ans

    

   
        
        
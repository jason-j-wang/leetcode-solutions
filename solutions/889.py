#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/?envType=daily-question&envId=2025-02-23
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre_idx = 0
        self.post_idx = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, postorder)

    def build(self, preorder, postorder):
        node = TreeNode(preorder[self.pre_idx])
        self.pre_idx += 1

        if node.val != postorder[self.post_idx]:
            node.left = self.build(preorder, postorder)

        if node.val != postorder[self.post_idx]:
            node.right = self.build(preorder, postorder)

        self.post_idx += 1
        return node

        


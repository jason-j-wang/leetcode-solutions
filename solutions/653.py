#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left_branch = []
        right_branch = []

        self.push_left(left_branch, root)
        self.push_right(right_branch, root)
        left, right = self.next_left(left_branch), self.next_right(right_branch)

        while left < right:
            if left + right == k:
                return True
            elif left + right < k:
                left = self.next_left(left_branch)
            else:
                right= self.next_right(right_branch)
        return False

    def push_left(self, stack, node):
        while node:
            stack.append(node)
            node = node.left

    def push_right(self, stack, node):
        while node:
            stack.append(node)
            node = node.right

    def next_left(self, stack):
        node = stack.pop()
        self.push_left(stack, node.right)
        return node.val

    def next_right(self, stack):
        node = stack.pop()
        self.push_right(stack, node.left)
        return node.val        
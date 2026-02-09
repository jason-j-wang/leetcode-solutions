#https://leetcode.com/problems/balance-a-binary-search-tree/description/?envType=daily-question&envId=2026-02-09
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def search(node):
            if node is None:
                return

            search(node.left)
            values.append(node.val)
            search(node.right)

        search(root)

        def create_tree(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            v = values[mid]
            t = TreeNode(v)

            t.left = create_tree(l, mid - 1)
            t.right = create_tree(mid + 1, r)

            return t
        return create_tree(0, len(values) - 1)
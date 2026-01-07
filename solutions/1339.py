#https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/?envType=daily-question&envId=2026-01-07
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        total_sum = 0
        mod = 10 ** 9 + 7

        while q:
            node = q.popleft()
            total_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return max(self.solve(root.left, total_sum)[0], self.solve(root.right, total_sum)[0]) % mod

        
    def solve(self, node, total):
        if node is None:
            return (0, 0)


        local_sum = node.val

        bl, sl = self.solve(node.left, total)
        br, sr = self.solve(node.right, total)

        local_sum += sl + sr
        best = max(bl, br, local_sum * (total - local_sum))

        return (best, local_sum)
        

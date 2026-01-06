#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=daily-question&envId=2026-01-06
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1

        max_sum = -math.inf
        max_level = 1

        while q:
            cur = 0
            num = len(q)
            for _ in range(num):
                node = q.popleft()
                cur += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            if cur > max_sum:
                max_sum = cur
                max_level = level

            level += 1

        return max_level
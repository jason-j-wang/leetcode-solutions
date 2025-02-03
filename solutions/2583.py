#https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/?envType=daily-question&envId=2025-02-03
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = []
        level_sums = []

        if root == None:
            return -1

        q.append(root)

        cur_sum = 0
        level_size = len(q)
        while q:
            node = q.pop(0)
            level_size -= 1

            cur_sum += node.val
            if node.left != None:
                q.append(node.left)
            
            if node.right != None:
                q.append(node.right)
            
            if level_size == 0:
                level_sums.append(cur_sum)
                cur_sum = 0
                level_size = len(q)
        
        if len(level_sums) < k:
            return -1

        level_sums.sort()
        level_sums = level_sums[::-1]
        
        return level_sums[k-1]

        
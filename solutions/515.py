#https://leetcode.com/problems/find-largest-value-in-each-tree-row/?envType=daily-question&envId=2025-01-26
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if root == None:
            return ans

        q = deque()
        q.append(root)
 

        while q:
            level = len(q)
            m = -float("inf")

            for i in range(level):
                node = q.popleft()
                if node.val > m:
                    m = node.val

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            ans.append(m)
        return ans
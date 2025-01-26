#https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/?envType=daily-question&envId=2025-01-26
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        cur_level = 0
        q = deque()
        q.append(root)

        while q:
            nodes = 2 ** cur_level
           
            values = [n.val for n in q]
            values.reverse()

            for i in range(nodes):
                node = q.popleft()
                if cur_level % 2 == 1:
                    node.val = values[i]

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            cur_level += 1
            
        return root


        
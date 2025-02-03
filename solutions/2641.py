#https://leetcode.com/problems/cousins-in-binary-tree-ii/description/?envType=daily-question&envId=2025-02-03
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = []
        root.val = 0
        if root == None:
            return root

        if root.left == None and root.right == None:
            return root

        if root.left == None:
            q.append(TreeNode(0))
        else:
            q.append(root.left)

        if root.right == None:
            q.append(TreeNode(0))
        else:
            q.append(root.right)

        while q:
            level_size = len(q)
            level_sum = 0
            level_nodes = []

            for i in range(level_size):
                node = q.pop(0)
                level_sum += node.val
                level_nodes.append(node)
                if node.val != 0 and (node.right != None or node.left != None):
                    if node.left == None:
                        q.append(TreeNode(0))
                    else:
                        q.append(node.left)

                    if node.right == None:
                        q.append(TreeNode(0))
                    else:
                        q.append(node.right)

            
            for i in range(0, level_size, 2):
                node1 = level_nodes[i]
                node2 = level_nodes[i+1]
                local_sum = node1.val + node2.val
                new_sum = level_sum - local_sum
                node1.val = new_sum
                node2.val = new_sum
            
        return root



#https://leetcode.com/problems/flip-equivalent-binary-trees/description/?envType=daily-question&envId=2025-02-03
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True

        if root1 == None or root2 == None:
            return False


        if root1.val == root2.val:
            possible_flip = False
            if (root1.left == None and root2.left == None) or (root1.right == None and root2.right == None):
                return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            elif (root1.left == None and root2.left != None) or (root1.left != None and root2.left == None):
                possible_flip = True
            elif (root1.right == None and root2.right != None) or (root1.right != None and root2.right == None):
                possible_flip = True
            elif (root1.left.val != root2.left.val or root1.right.val != root2.right.val):
                possible_flip = True

            if possible_flip:
                temp = root1.left
                root1.left = root1.right
                root1.right = temp
                
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        else:
            return False
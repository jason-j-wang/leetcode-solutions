#https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/?envType=daily-question&envId=2025-01-26
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = deque()
        q.append(root)
        total = 0

        while q:
            level = len(q)
            arr = []

            for i in range(level):
                node = q.popleft()
                arr.append(node.val)

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            total += self.minSwaps(arr)
        return total



    def minSwaps(self, arr):
        target_arr = sorted(arr)
        d = {}
        for i, num in enumerate(arr):
            d[num] = i

        s = 0
        swaps = 0

        while s < len(arr):
            if arr[s] == target_arr[s]:
                s += 1
            else:
                idx = d[target_arr[s]]
                temp = arr[s]

                arr[s] = target_arr[s]
                arr[idx] = temp
                d[temp] = idx
                swaps += 1
                s += 1

        return swaps

        
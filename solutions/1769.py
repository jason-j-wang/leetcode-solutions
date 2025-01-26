#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/?envType=daily-question&envId=2025-01-26
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        right_shift = 0
        left = 0
        left_shift = 0
        right = 0

        for i in range(len(boxes)):
            if boxes[i] == '1':
                right_shift += i
                right += 1


        ans = [0] * len(boxes)

        for i in range(len(boxes)):
            ans[i] = left_shift + right_shift - i * right
            left_shift += left
            if boxes[i] == '1':
                left_shift += 1
                left += 1
                right -= 1
                right_shift -= i
        return ans
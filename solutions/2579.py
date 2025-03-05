#https://leetcode.com/problems/count-total-number-of-colored-cells/?envType=daily-question&envId=2025-03-05
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n-1) + 1
#https://leetcode.com/problems/maximal-rectangle/description/?envType=daily-question&envId=2026-01-11
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])

        heights = [0 for _ in range(n + 1)]
        ans = 0

        for i in range(len(matrix)):
            stack = []
            for j in range(n + 1):
                if j < n and matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

                while stack and heights[stack[-1]] > heights[j]:
                    h = heights[stack.pop()]
                    w = j if not stack else j - stack[-1] - 1
                    ans = max(ans, w * h)
                
                stack.append(j)
        return ans



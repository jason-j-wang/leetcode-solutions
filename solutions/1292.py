#https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/?envType=daily-question&envId=2026-01-19
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])

        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1]
        
        ans = 0
        edge = min(m, n)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(ans + 1, edge + 1):
                    if i + k - 1 <= m and j + k - 1 <= n:
                        if prefix[i + k - 1][j + k - 1] - prefix[i - 1][j + k - 1] - prefix[i + k - 1][j-1] + prefix[i-1][j-1] <= threshold:
                            ans += 1
                        else:
                            break


        return ans

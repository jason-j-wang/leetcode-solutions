#https://leetcode.com/problems/increment-submatrices-by-one/description/?envType=daily-question&envId=2025-11-14
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        prefix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            prefix[r1][c1] += 1
            prefix[r1][c2 + 1] -= 1
            prefix[r2 + 1][c1] -= 1
            prefix[r2 + 1][c2 + 1] += 1

        ans = [[0 for _ in range(n)] for _ in range(n)]
        print(prefix)

        for row in range(n):
            cur = 0

            for col in range(n):
                cur += prefix[row][col]
                
                ans[row][col] = cur
                if row > 0:
                    ans[row][col] += ans[row-1][col]
        return ans
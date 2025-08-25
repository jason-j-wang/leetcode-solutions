#https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n = len(mat)
        m = len(mat[0])

        rev = False
        #row wise
        for start in range(0, n):
            segment = []
            i = start
            j = 0

            while i >= 0 and j < m:
                segment.append(mat[i][j])
                i -= 1
                j += 1

            if rev:
                segment.reverse()

            ans += segment
            rev = not rev

        #col wise
        if m != 1:
            for start in range(1, m):
                segment = []
                i = n - 1
                j = start

                while i >= 0 and j < m:
                    segment.append(mat[i][j])
                    i -= 1
                    j += 1

                if rev:
                    segment.reverse()

                ans += segment
                rev = not rev
        return ans
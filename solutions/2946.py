#https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/?envType=daily-question&envId=2026-03-27
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] != mat[i][(j + k) % m]:
                    return False
        return True
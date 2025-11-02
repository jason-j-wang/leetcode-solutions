#https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/?envType=daily-question&envId=2025-11-02
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        graph = [[0 for _ in range(n)] for _ in range(m)]
        count = [n * m - len(guards) - len(walls)]

        for r, c in guards:
            graph[r][c] = 1

        for r, c in walls:
            graph[r][c] = 2

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c, dir):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if graph[r][c] == 1 or graph[r][c] == 2:
                return

            if graph[r][c] == 0:
                count[0] -= 1

            graph[r][c] = -1
            dfs(r + dir[0], c + dir[1], dir)


        for r, c in guards:
            for dir in dirs:
                dfs(r + dir[0], c + dir[1], dir)
        return count[0]
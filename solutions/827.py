#https://leetcode.com/problems/making-a-large-island/description/?envType=daily-question&envId=2025-01-31
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        largest = -1
        islands = {}
        island_num = 2

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = self.bfs(grid, island_num, i, j)
                    largest = max(area, largest)
                    islands[island_num] = area
                    island_num += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    largest = max(largest, self.bridge(grid, islands, i, j))
        
        return largest

    def bfs(self, grid, num, x, y):
        n = len(grid)
        m = len(grid[0])
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        q = deque()
        q.append((x, y))
        grid[x][y] = num
        area = 0

        while q:
            area += 1
            i, j = q.popleft()

            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m and grid[new_i][new_j] == 1:
                    q.append((new_i, new_j))
                    grid[new_i][new_j] = num

        return area

    def bridge(self, grid, areas, i, j):
        n = len(grid)
        m = len(grid[0])
        touching_islands = []
        area = 0
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        for d in directions:
            new_i = i + d[0]
            new_j = j + d[1]
            if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m and grid[new_i][new_j] > 1:
                if grid[new_i][new_j] not in touching_islands:
                    touching_islands.append(grid[new_i][new_j])

        for island in touching_islands:
            area += areas[island]
        return area + 1


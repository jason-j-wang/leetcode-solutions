#https://leetcode.com/problems/last-day-where-you-can-still-cross/description/?envType=daily-question&envId=2025-12-31
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        q = []

        days = [[0 for _ in range(col)] for _ in range(row)]

        for day, (r, c) in enumerate(cells):
            if c == 1:
                heapq.heappush(q, (day + 1, r, c))

            days[r-1][c-1] = day + 1

        max_day = 0

        while q:
            day, r, c = heapq.heappop(q)
            max_day = max(max_day, day)
            if c == col:
                return max_day - 1

            if days[r-1][c-1] == -1:
                continue

            days[r-1][c-1] = -1
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if i > 0 and i <= row and j > 0 and j <= col and days[i-1][j-1] != -1:
                        heapq.heappush(q, (days[i-1][j-1], i, j))
        
        return max_day - 1

        
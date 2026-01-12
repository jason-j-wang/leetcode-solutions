#https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-01-12
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]

            time += max(abs(x1 - x2), abs(y1 - y2))
        return time
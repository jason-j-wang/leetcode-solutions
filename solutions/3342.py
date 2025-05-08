#https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description/?envType=daily-question&envId=2025-05-08
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dists = [[float("inf") for i in range(m)] for i in range(n)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = [(0, 0, 0, True)]

        while q:
            time, i, j, t = heapq.heappop(q)

            if i == n - 1 and j == m - 1:
                return time    

            for v, h in dirs:
                next_i, next_j = i + v, j + h

                if next_i >= 0 and next_i < n and next_j >= 0 and next_j < m:
                    new_time = max(time, moveTime[next_i][next_j])
                    new_time = new_time + 1 if t else new_time + 2
                    if new_time < dists[next_i][next_j]:
                        dists[next_i][next_j] = new_time
                        heapq.heappush(q, (new_time, next_i, next_j, not t))
            

        return -1
#https://leetcode.com/problems/min-cost-to-connect-all-points/description/?envType=problem-list-v2&envId=minimum-spanning-tree
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = [False for i in range(len(points))]
        queue = [(0, 0)]
        total_weight = 0
        points_met = 0

        while queue:
            weight, index = heapq.heappop(queue)
            if visited[index]:
                continue

            total_weight += weight
            visited[index] = True
            points_met += 1

            if points_met == len(points):
                return total_weight

            for i in range(len(points)):
                if i != index and not visited[i]:
                    heapq.heappush(queue, (self.manhattan_distance(points[i], points[index]), i))

        return total_weight


    def manhattan_distance(self, p1, p2) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
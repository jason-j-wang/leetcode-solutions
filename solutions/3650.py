#https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/description/?envType=daily-question&envId=2026-01-27
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for x, y, w in edges:
            adj[x].append((w, y))
            adj[y].append((2 * w, x))

        dist = [inf for _ in range(n)]
        dist[0] = 0

        q = [(0, 0)]

        while q:
            cost, node = heapq.heappop(q)

            if node == n - 1:
                return cost

            if dist[node] < cost:
                continue

            for w, next in adj[node]:
                new_cost = cost + w
                if new_cost < dist[next]:
                    dist[next] = new_cost
                    heapq.heappush(q, (new_cost, next))
        return -1
        
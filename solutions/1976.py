#https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/?envType=daily-question&envId=2025-03-23
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for v1, v2, w in roads:
            adj[v1].append((w, v2))
            adj[v2].append((w, v1))

        q = [(0, 0)]
        dist = [float("inf") for i in range(n)]
        counts = [0 for i in range(n)]
        dist[0] = 0
        counts[0] = 1

        while q:
            w, node = heapq.heappop(q)
            
            for next_weight, next in adj[node]:
                if w + next_weight < dist[next]:
                    dist[next] = w + next_weight
                    counts[next] = counts[node]
                    heapq.heappush(q, (w + next_weight, next))

                elif w + next_weight == dist[next]:
                    counts[next] = (counts[next] + counts[node]) % (10 ** 9 + 7)

        return counts[n-1]  

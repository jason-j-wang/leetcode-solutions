#https://leetcode.com/problems/count-the-number-of-complete-components/description/?envType=daily-question&envId=2025-03-22
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = [False for i in range(n)]

        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += self.bfs(adj, i, visited)
        return ans

    def bfs(self, adj, start, visited):
        nodes = 0
        edges = 0
        q = deque([start])
        visited[start] = True

        while q:
            node = q.popleft()
            nodes += 1
            
            for next in adj[node]:
                edges += 1
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
        return 1 if edges == nodes * (nodes - 1) else 0
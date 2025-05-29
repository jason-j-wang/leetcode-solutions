#https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        _, n1_1 = self.bfs(adj1, 0, n)
        dia1, _ = self.bfs(adj1, n1_1, n)

        _, n2_1 = self.bfs(adj2, 0, m)
        dia2, _ = self.bfs(adj2, n2_1, m)

        return max(dia1, dia2, (dia1 + 1) // 2 + (dia2 + 1) // 2 + 1)

    def bfs(self, adj, start, n):
        q = deque([start])
        visited = [False for _ in range(n)]
        visited[start] = True
        dist = 0
        farthest = -1

        while q:
            num_nodes = len(q)

            for _ in range(num_nodes):
                node = q.popleft()
                farthest = node

                for next in adj[node]:
                    if not visited[next]:
                        visited[next] = True
                        q.append(next)
            dist += 1

        return dist - 1, farthest
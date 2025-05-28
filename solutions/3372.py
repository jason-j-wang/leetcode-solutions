#https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description/?envType=daily-question&envId=2025-05-28
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        best_second = 0
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

        for i in range(m):
            best_second = max(best_second, self.bfs(i, adj2, k-1, m))

        ans = [self.bfs(i, adj1, k, n) + best_second for i in range(n)]
        return ans

        
    def bfs(self, start, adj, k, n):
        q = deque([start])
        dist = 0
        nodes = 0

        visited = [False for _ in range(n)]
        visited[start] = True

        while q and dist <= k:
            num = len(q)

            for i in range(num):
                node = q.popleft()
                nodes += 1
                for next in adj[node]:
                    if not visited[next]:
                        q.append(next)
                        visited[next] = True
            dist += 1
        return nodes

    
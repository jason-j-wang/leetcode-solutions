#https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description/?envType=daily-question&envId=2025-05-29
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
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

        edge2_odd, edge2_even, _, _ = self.bfs(adj2, True, m)
        edge1_odd, edge1_even, odd_nodes, even_nodes = self.bfs(adj1, False, n)

        best_second = max(edge2_odd, edge2_even)

        ans = []
        for i in range(n):
            if i in odd_nodes:
                ans.append(edge1_odd + best_second)
            else:
                ans.append(edge1_even + best_second)
        return ans

        
    def bfs(self, adj, is_odd, n):
        q = deque([0])
        odd_nodes = set()
        even_nodes = set()
        odd_count = 0
        even_count = 0

        visited = [False for _ in range(n)]
        visited[0] = True

        while q:
            num = len(q)

            for i in range(num):
                node = q.popleft()
                if is_odd:
                    odd_count += 1
                    odd_nodes.add(node)
                else:
                    even_count += 1
                    even_nodes.add(node)
                for next in adj[node]:
                    if not visited[next]:
                        q.append(next)
                        visited[next] = True
            is_odd = not is_odd
        return odd_count, even_count, odd_nodes, even_nodes
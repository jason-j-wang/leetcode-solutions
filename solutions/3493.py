#https://leetcode.com/problems/properties-graph/description/
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)

        adj = [[] for i in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                if self.intersect(properties[i], properties[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False for i in range(n)]
        ans = 0
        for i in range(n):
            if not visited[i]:
                self.bfs(adj, i, visited)
                ans += 1

        return ans

    def bfs(self, adj, start, visited):
        q = deque([start])

        visited[start] = True

        while q:
            node = q.popleft()
            for next in adj[node]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
        
        

    def intersect(self, a, b):
        a = set(a)
        b = set(b)
        total = 0

        for num in a:
            if num in b:
                total += 1
        return total
        
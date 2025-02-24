#https://leetcode.com/problems/most-profitable-path-in-a-tree/description/?envType=daily-question&envId=2025-02-24
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        adj = [[] for i in range(len(edges) + 1)]

        for a, b in edges:
            adj[b].append(a)
            adj[a].append(b)

        bob_path = {}
        visited = [False for i in range(n)]
        self.find_bob(adj, bob, bob_path, visited, 0)

        visited = [False for i in range(n)]
        q = deque()
        best = -float("inf")
        q.append((0, 0))
        time = 0

        while q:
            level = len(q)
            for i in range(level):
                node, cur_amount = q.popleft()
                visited[node] = True
                if node in bob_path:
                    if time < bob_path[node]:
                        cur_amount += amount[node]
                    elif time == bob_path[node]:
                        cur_amount += amount[node] // 2
                else:
                    cur_amount += amount[node]
                leaf = True
                for next in adj[node]:
                    if not visited[next]:
                        q.append((next, cur_amount))
                        leaf = False

                if leaf:
                    best = max(best, cur_amount)
            time += 1
        return best
        
    def find_bob(self, adj, node, bob_path, visited, time):
        visited[node] = True

        if node == 0:
            bob_path[node] = time
            return True

        for next in adj[node]:
            if not visited[next]:
                if self.find_bob(adj, next, bob_path, visited, time + 1):
                    bob_path[node] = time
                    return True
        return False

        
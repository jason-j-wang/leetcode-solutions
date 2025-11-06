#https://leetcode.com/problems/power-grid-maintenance/description/?envType=daily-question&envId=2025-11-06
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False for _ in range(c + 1)]
        offline = [False for _ in range(c + 1)]
        group = defaultdict(list)
        group_map = {}

        def bfs(node, group_number):
            q = deque([node])

            while q:
                node = q.popleft()
                visited[node] = True
                heapq.heappush(group[group_number], node)
                group_map[node] = group_number

                for n in adj[node]:
                    if not visited[n]:
                        visited[n] = True
                        q.append(n)
        g = 0
        for i in range(1, c + 1):
            if not visited[i]:
                bfs(i, g)
                g += 1

        ans = []
        for i, (command, node) in enumerate(queries):
            if command == 2:
                offline[node] = True
                continue

            if not offline[node]:
                ans.append(node)
                continue

            q = group[group_map[node]]
            while q and offline[q[0]]:
                heapq.heappop(q)

            if not q:
                ans.append(-1)
            else:
                ans.append(q[0])
        return ans
            
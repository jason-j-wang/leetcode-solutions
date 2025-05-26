#https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/?envType=daily-question&envId=2025-05-26
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        col = [ord(c) - ord('a') for c in colors]

        adj = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        dp = [[0 for _ in range(26)] for _ in range(n)]

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i][col[i]] = 1

        seen = 0
        ans = 0

        while q:
            node = q.popleft()
            seen += 1

            cur_best = max(dp[node])
            if cur_best > ans:
                ans = cur_best

            for next in adj[node]:
                next_counts = dp[next]
                next_color = col[next]
                for c in range(26):
                    count = dp[node][c]
                    if c == next_color:
                        count += 1

                    if count > next_counts[c]:
                        next_counts[c] = count

                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)

            dp[node] = None

        return ans if seen == n else -1

        
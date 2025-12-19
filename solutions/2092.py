#https://leetcode.com/problems/find-all-people-with-secret/description/?envType=daily-question&envId=2025-12-19
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        same_meetings = defaultdict(list)

        for x, y, t in meetings:
            same_meetings[t].append((x, y))

        parent = [p for p in range(n)]
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]


        def union(x, y):
            rootx, rooty = find(x), find(y)

            if rootx == rooty:
                return

            if rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
            elif rank[rooty] > rank[rootx]:
                parent[rootx] = rooty
            else:
                parent[rooty] = rootx
                rank[rootx] += 1

        def reset(x):
            parent[x] = x
            rank[x] = 0

        def conn(x, y):
            return find(x) == find(y)

        union(0, firstPerson)

        for t in same_meetings:
            for x, y in same_meetings[t]:
                union(x, y)

            for x, y in same_meetings[t]:
                if not conn(x, 0):
                    reset(x)
                    reset(y)

        return [i for i in range(n) if conn(i, 0)]
            
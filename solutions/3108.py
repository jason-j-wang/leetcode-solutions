#https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/?envType=daily-question&envId=2025-03-20
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = [-1 for i in range(n)]
        cost = [-1 for i in range(n)]
        depth = [0 for i in range(n)]

        for start, end, _ in edges:
            self.union(start, end, parent, depth)

        for start, _, weight in edges:
            root = self.find(start, parent)
            cost[root] &= weight

        ans = []
        for start, end in query:
            root1 = self.find(start, parent)
            root2 = self.find(end, parent)
            if root1 != root2 :
                ans.append(-1)
            else:
                ans.append(cost[root1])
        return ans


    def find(self, node, parent):
        if parent[node] == -1:
            return node
        parent[node] = self.find(parent[node], parent)
        return parent[node]

    def union(self, node1, node2, parent, depth):
        root1 = self.find(node1, parent)
        root2 = self.find(node2, parent)

        if root1 == root2:
            return

        if depth[root1] < depth[root2]:
            parent[root1] = root2
        elif depth[root1] > depth[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            depth[root2] += 1


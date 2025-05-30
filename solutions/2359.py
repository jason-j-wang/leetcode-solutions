#https://leetcode.com/problems/find-closest-node-to-given-two-nodes/?envType=daily-question&envId=2025-05-30
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [-1 for _ in range(n)]
        dist2 = [-1 for _ in range(n)]

        dist1[node1] = 0
        dist2[node2] = 0

        next = edges[node1]
        dist = 1

        while next != -1 and dist1[next] == -1:
            dist1[next] = dist
            dist += 1
            next = edges[next]

        next = edges[node2]
        dist = 1

        while next != -1 and dist2[next] == -1:
            dist2[next] = dist
            dist += 1
            next = edges[next]

        ans = -1

        for i in range(n):
            if dist1[i] > -1 and dist2[i] > -1:
                d = max(dist1[i], dist2[i])
                if ans == -1 or d < max(dist1[ans], dist2[ans]):
                    ans = i

        return ans

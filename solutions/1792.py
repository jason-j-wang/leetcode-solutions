#https://leetcode.com/problems/maximum-average-pass-ratio/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        t = 0
        perfects = 0

        for c in classes:
            ratio = c[0] / c[1]
            next_ratio = (c[0] + 1) / (c[1] + 1)

            if ratio < 1:
                heapq.heappush(pq, [-(next_ratio - ratio), c[0], c[1]])
            else:
                t += 1
                perfects += 1
        if not pq:
            return 1

        for i in range(extraStudents):
            _, passed, total = heapq.heappop(pq)

            new_ratio = (passed + 1) / (total + 1)
            next_ratio = (passed + 2) / (total + 2)
            heapq.heappush(pq, [-(next_ratio - new_ratio), passed + 1, total + 1])

        for i in range(len(pq)):
            t += pq[i][1] / pq[i][2]

        return t / (len(pq) + perfects)
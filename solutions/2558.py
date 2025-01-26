#https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []

        for g in gifts:
            heapq.heappush(pq, -g)

        for i in range(k):
            g = heapq.heappop(pq)
            g *= -1
 

            amount = int(sqrt(g) // 1)

            heapq.heappush(pq, -amount)

        total = 0

        while pq:
            total -= heapq.heappop(pq)
        return total
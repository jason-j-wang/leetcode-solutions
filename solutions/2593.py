#https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False for i in range(len(nums))]
        score = 0
        pq = []

        for i, n in enumerate(nums):
            heapq.heappush(pq, [n, i])

        
        while pq:
            num, idx = heapq.heappop(pq)

            if marked[idx]:
                continue

            marked[idx] = True
            score += num

            if idx - 1 >= 0:
                marked[idx - 1] = True
            if idx + 1 < len(nums):
                marked[idx + 1] = True

        return score
        
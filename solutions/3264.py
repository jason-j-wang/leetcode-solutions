#https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []

        for i in range(len(nums)):
            heapq.heappush(pq, [nums[i], i])

        for _ in range(k):
            num, idx = heapq.heappop(pq)
            num *= multiplier
            nums[idx] = num
            heapq.heappush(pq, [num, idx])

        return nums
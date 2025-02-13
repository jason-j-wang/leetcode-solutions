#https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-13
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)
        while True:
            first = heapq.heappop(nums)

            if first >= k:
                return ans

            second = heapq.heappop(nums)
            ans += 1
            heapq.heappush(nums, first * 2 + second)
        return 0
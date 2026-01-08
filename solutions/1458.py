#https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/?envType=daily-question&envId=2026-01-08
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        m = len(nums2)

        dp = [[-inf for _ in range(m)] for _ in range(n)]

        def solve(p1, p2, empty):
            if p1 == n or p2 == m:
                return 0 if not empty else -inf

            if dp[p1][p2] != -inf:
                return dp[p1][p2]

            cur = max(solve(p1 + 1, p2, empty), solve(p1, p2 + 1, empty), nums1[p1] * nums2[p2] + solve(p1 + 1, p2 + 1, False), nums1[p1] * nums2[p2])

            dp[p1][p2] = cur
            return cur

        solve(0, 0, True)
        return dp[0][0]
#https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/?envType=daily-question&envId=2025-07-08
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()

        #dp[k][i]
        dp = [[-1 for i in range(n)] for j in range(k+1)]

        return self.solve(events, 0, k, dp, n)


    def solve(self, events, i, k, dp, n):
        if k == 0 or i == n:
            return 0

        if dp[k][i] != -1:
            return dp[k][i]

        end = events[i][1]

        left = i
        right = n 

        while left < right:
            mid = left + (right - left) // 2

            if events[mid][0] <= end:
                left = mid + 1
            else:
                right = mid

        dp[k][i] = max(self.solve(events, i + 1, k, dp, n), events[i][2] + self.solve(events, left, k - 1, dp, n))
        return dp[k][i]

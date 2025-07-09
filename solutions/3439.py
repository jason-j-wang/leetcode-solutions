#https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/editorial/?envType=daily-question&envId=2025-07-09
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        largest_diff = 0
        idx = 0
        n = len(startTime)

        diffs = [0 for _ in range(n+1)]
        diffs[0] = startTime[0]
        diffs[n] = eventTime - endTime[n-1]

        for i in range(1, n):
            diffs[i] = startTime[i] - endTime[i-1]

        ans = sum(diffs[0:k+1])
        cur = ans

        for i in range(k + 1, n+1):
            cur += diffs[i]
            cur -= diffs[i - k - 1]

            if cur > ans:
                ans = cur
        return ans

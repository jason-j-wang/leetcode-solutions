#https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/?envType=daily-question&envId=2025-02-27
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        nums = {}
        for i in range(n):
            nums[arr[i]] = i

        dp = [[0 for i in range(n)] for i in range(n)]
        ans = 0

        for cur in range(n-1, -1, -1):
            for before in range(cur-1, -1, -1):
                num = arr[cur] + arr[before]
                if num not in nums:
                    dp[before][cur] = 1
                else:
                    idx = nums[num]
                    dp[before][cur] = dp[cur][idx] + 1
                    ans = max(ans, dp[before][cur])
        ans += 1
        return ans if ans >= 3 else 0

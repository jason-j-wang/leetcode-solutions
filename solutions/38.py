#https://leetcode.com/problems/count-and-say/description/?envType=daily-question&envId=2025-04-18
class Solution:
    def countAndSay(self, n: int) -> str:
        dp = [0 for i in range(n)]
        dp[0] = "1"
        for i in range(1, n):
            dp[i] = self.rle(dp[i-1])
        return dp[-1]

    def rle(self, n):
        res = ""
        i = 0
        count = 0

        while i < len(n):
            if i == 0 or n[i] == n[i-1]:
                count += 1

            else:
                res += str(count) + n[i-1]
                count = 1
            i += 1

        res += str(count) + n[i-1]
        return res

        
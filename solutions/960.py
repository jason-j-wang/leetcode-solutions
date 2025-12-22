#https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/?envType=daily-question&envId=2025-12-22
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])

        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if all(word[i] <= word[j] for word in strs):
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)
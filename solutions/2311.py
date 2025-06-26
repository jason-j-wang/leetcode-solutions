#https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/description/?envType=daily-question&envId=2025-06-26
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        num = 0
        count = 0
        bits = k.bit_length()
        n = len(s)

        for exp in range(n):
            i = n - 1 - exp

            if s[i] == "1":
                if exp < bits and num + 2 ** exp <= k:
                    num += 2 ** exp
                    count += 1
            else:
                count += 1
        return count

#https://leetcode.com/problems/number-of-substrings-with-only-1s/description/?envType=daily-question&envId=2025-11-16
class Solution:
    def numSub(self, s: str) -> int:
        cur_ones = 0
        ans = 0
        mod = 10 ** 9 + 7

        for c in s:
            if c == "0":
                ans = (ans + (cur_ones * (cur_ones + 1) // 2)) % mod
                cur_ones = 0
            else:
                cur_ones += 1

        ans = (ans + (cur_ones * (cur_ones + 1) // 2)) % mod

        return ans
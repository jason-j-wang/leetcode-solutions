#https://leetcode.com/problems/unique-length-3-palindromic-subsequences/?envType=daily-question&envId=2025-01-26
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for l in letters:
            left = s.index(l)
            right = s.rindex(l)
            between = set()

            for i in range(left + 1, right):
                between.add(s[i])
            ans += len(between)

        return ans
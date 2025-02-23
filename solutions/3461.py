#https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            new = ""
            for i in range(1, len(s)):
                new += str((int(s[i]) + int(s[i-1])) % 10)

            s = new
        return s[0] == s[1]
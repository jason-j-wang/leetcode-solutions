#https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05
class Solution:
    def minOperations(self, s: str) -> int:
        s1 = 0
        s2 = 0

        s1_zero = True
        s2_zero = False

        for c in s:
            if c == "0":
                s1 += 0 if s1_zero else 1
                s2 += 0 if s2_zero else 1
            else:
                s1 += 1 if s1_zero else 0
                s2 += 1 if s2_zero else 0

            s1_zero = not s1_zero
            s2_zero = not s2_zero

        return min(s1, s2)

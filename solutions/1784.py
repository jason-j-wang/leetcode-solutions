#https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/?envType=daily-question&envId=2026-03-06
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        no_more_ones = False
        for i in range(1, len(s)):
            if s[i] == "0":
                if not no_more_ones:
                    no_more_ones = True
            if s[i] == "1" and no_more_ones:
                return False
        return True
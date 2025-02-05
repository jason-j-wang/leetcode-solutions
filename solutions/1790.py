#https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=daily-question&envId=2025-02-05
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)

        if len(diffs) == 1 or len(diffs) > 2:
            return False
        
        if not diffs:
            return True
        
        return s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]
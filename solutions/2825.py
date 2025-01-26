#https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/?envType=daily-question&envId=2025-01-26
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s1 = len(str1)
        s2 = len(str2)

        cur = 0

        for i in range(s1):
            if cur < s2 and (str1[i] == str2[cur] or ord(str1[i]) + 1 == ord(str2[cur]) or ord(str1[i]) == ord(str2[cur]) + 25):
                cur += 1

        return cur == s2
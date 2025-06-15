#https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/?envType=daily-question&envId=2025-06-15
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_num = s
        min_1 = s
        min_0 = s
        pos = 0
        while pos < len(s) and s[pos] == "9":
            pos += 1
        if pos < len(s):
            max_num = max_num.replace(s[pos], "9")
        
        min_1 = min_1.replace(s[0], "1")

        pos = 0
        while pos < len(s) and (s[pos] == s[0] or s[pos] == "0"):
            pos += 1
        if pos < len(s):
            min_0 = min_0.replace(s[pos], "0")
        

        return int(max_num) - min(int(min_1), int(min_0))

#https://leetcode.com/problems/maximum-69-number/description/?envType=daily-question&envId=2025-08-16
class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = ""
        sn = str(num)
        for i in range(len(sn)):
            if sn[i] == "6":
                ans += "9"
                ans += sn[i+1:]
                return int(ans)
            ans += sn[i]
        return int(ans)
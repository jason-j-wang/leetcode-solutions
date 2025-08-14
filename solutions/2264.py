#https://leetcode.com/problems/largest-3-same-digit-number-in-string/?envType=daily-question&envId=2025-08-14
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = "0"

        for i in range(2, len(num)):
            if num[i] == num[i-1] and num[i-1] == num[i-2]:
                if int(num[i]) >= int(ans) % 10:
                    ans = num[i] * 3
        return ans if ans != "0" else ""
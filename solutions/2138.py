#https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/?envType=daily-question&envId=2025-06-22
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        g = ""

        for i in range(len(s)):
            g += s[i]

            if (i + 1) % k == 0:
                ans.append(g)
                g = ""

        if len(g) > 0:
            g += fill * (k - len(g))
            ans.append(g)
        return ans
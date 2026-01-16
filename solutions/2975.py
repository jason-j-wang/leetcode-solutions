#https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/?envType=daily-question&envId=2026-01-16
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9 + 7
        if m == n:
            return ((m - 1) ** 2) % mod

        ans = -1
        hFences.append(m)
        vFences.append(n)

        hFences.append(1)
        vFences.append(1)

        hFences.sort()
        vFences.sort()

        seen = {}

        for h in hFences:
            for v in vFences:
                min_edge = min(h, v)
                offset = (h - min_edge, v - min_edge)
                if offset in seen:
                    ho, vo = seen[offset]
                    ans = max(ans, (h - ho) ** 2)
                else:
                    seen[offset] = (h, v)

        return ans % mod if ans >= 0 else ans
#https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/?envType=daily-question&envId=2026-01-15
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        curh = 1
        besth = 1

        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i-1] + 1:
                curh += 1
            else:
                besth = max(besth, curh + 1)
                curh = 1
        besth = max(besth, curh + 1)

        curv = 1
        bestv = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i-1] + 1:
                curv += 1
            else:
                bestv = max(bestv, curv + 1)
                curv = 1
        bestv = max(bestv, curv + 1)
        return min(besth, bestv) ** 2
        
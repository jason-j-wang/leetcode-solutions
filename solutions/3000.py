#https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag = 0
        area = 0

        for l, w in dimensions:
            d = sqrt(l * l + w * w)
            if d == diag:
                if l * w > area:
                    area = l * w
            elif d > diag:
                area = l * w
                diag = d
        return area
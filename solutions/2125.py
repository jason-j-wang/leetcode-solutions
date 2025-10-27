#https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2025-10-27
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        r1, r2 = 0, 0
        ans = 0

        for row in bank:
            r2 = row.count("1")
            ans += r1 * r2

            if r2 > 0:
                r1 = r2
                r2 = 0
            
        return ans

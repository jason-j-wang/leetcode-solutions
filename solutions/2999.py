#https://leetcode.com/problems/count-the-number-of-powerful-integers/description/?envType=daily-question&envId=2025-04-10
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        return self.solve(str(finish), s, limit) - self.solve(str(start-1), s, limit)
    

    def solve(self, end, s, limit):
        if len(end) < len(s):
            return 0

        if len(end) == len(s):
            return 1 if int(end) >= int(s) else 0

        ans = 0
        powers = len(end) - len(s)

        for i in range(powers):
            if limit < int(end[i]):
                ans += (limit + 1) ** (powers - i)
                return ans
            ans += int(end[i]) * ((limit + 1) ** (powers - 1 - i))

        if int(end[len(end) - len(s):]) >= int(s):
            ans += 1
        return ans
#https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        most = 0
        ans = 0

        for i in range(1, n+1):
            num = i
            s = 0

            while num != 0:
                s += num % 10
                num //= 10

            groups[s] += 1

            if groups[s] > most:
                most = groups[s]
                ans = 1
            elif groups[s] == most:
                ans += 1

        return ans
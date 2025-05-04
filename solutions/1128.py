#https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = [0 for _ in range(100)]
        ans = 0

        for a, b in dominoes:
            num = a * 10 + b if a <= b else b * 10 + a
            ans += counts[num]
            counts[num] += 1

        return ans
        
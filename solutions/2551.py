#https://leetcode.com/problems/put-marbles-in-bags/description/?envType=daily-question&envId=2025-03-31
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = []
        for i in range(len(weights)-1):
            pairs.append(weights[i]+weights[i+1])

        pairs.sort()
        ans = 0

        for i in range(k - 1):
            ans += pairs[-i - 1] - pairs[i]
        return ans
#https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
class Solution:
    def maxDifference(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        max_odd = -1
        min_even = 200

        for c in count:
            if count[c] % 2 == 0:
                min_even = min(min_even, count[c])
            else:
                max_odd = max(max_odd, count[c])
        return max_odd - min_even
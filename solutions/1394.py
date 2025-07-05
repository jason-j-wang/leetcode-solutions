#https://leetcode.com/problems/find-lucky-integer-in-an-array/submissions/1686708614/?envType=daily-question&envId=2025-07-05
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        ans = -1
        for c in counts:
            if c == counts[c] and c > ans:
                ans = c
        return ans
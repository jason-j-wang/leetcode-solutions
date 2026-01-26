#https://leetcode.com/problems/minimum-absolute-difference/?envType=daily-question&envId=2026-01-26
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_diff = inf
        for i in range(1, len(arr)):
            a, b = arr[i-1], arr[i]
            if b - a <  min_diff:
                ans = [[a, b]]
                min_diff = b - a
            elif b - a == min_diff:
                ans.append([a, b])
        return ans
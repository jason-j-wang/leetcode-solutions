#https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/?envType=daily-question&envId=2025-10-30
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)

        ans = target[0]

        for i in range(1, n):
            s = target[i] - target[i-1]
            if s > 0:
                ans += s
        return ans

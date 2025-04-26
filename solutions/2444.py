#https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/?envType=daily-question&envId=2025-04-26
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        last_max = -1
        last_min = -1
        left = 0

        for right, n in enumerate(nums):
            if n < minK or n > maxK:
                left = right + 1
            else:
                if n == maxK:
                    last_max = right
                if n == minK:
                    last_min = right
                
                ans += max(min(last_max, last_min) - left + 1, 0)
        return ans
                

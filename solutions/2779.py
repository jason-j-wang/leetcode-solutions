#https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0

        for right in range(len(nums)):
            while nums[left] + 2 * k < nums[right]:
                left += 1

            ans = max(ans, right - left + 1)

        return ans
        
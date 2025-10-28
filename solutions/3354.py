#https://leetcode.com/problems/make-array-elements-equal-to-zero/description/?envType=daily-question&envId=2025-10-28
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        ans = 0

        for num in nums:
            left += num
            right -= num

            if num == 0:
                if left - right == 0:
                    ans += 2
                elif abs(left - right) == 1:
                    ans += 1
        return ans
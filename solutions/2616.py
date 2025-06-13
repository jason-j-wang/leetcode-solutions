#https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/?envType=daily-question&envId=2025-06-13
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left = 0
        right = max(nums)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if self.validate(nums, mid, p):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans

        

    def validate(self, nums, threshold, p):
        count = 0
        i = 1
        while i < len(nums):
            if abs(nums[i] - nums[i-1]) <= threshold:
                count += 1
                i += 2
            else:
                i += 1

            if count >= p:
                return True
        return False
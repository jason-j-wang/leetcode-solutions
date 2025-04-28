#https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/?envType=daily-question&envId=2025-04-28
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        left = 0
        right = 0
        ans = 0

        while right < len(nums):
            cur_sum += nums[right]

            while cur_sum * (right - left + 1) >= k and left < right:
                cur_sum -= nums[left]
                left += 1

            if cur_sum * (right - left + 1) < k:
                ans += right - left + 1

            right += 1
        return ans

            
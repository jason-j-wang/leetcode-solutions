#https://leetcode.com/problems/count-the-number-of-good-subarrays/description/?envType=daily-question&envId=2025-04-16
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        ans = 0
        left = 0
        right = 0
        cur_pairs = 0

        while right < len(nums):
            counts[nums[right]] += 1
            c = counts[nums[right]]
            cur_pairs += c - 1


            while cur_pairs >= k:
                ans += len(nums) - right
                n = nums[left]
                counts[n] -= 1
                cur_pairs -= counts[n]
                left += 1
            right += 1
        return ans

            

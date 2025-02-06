#https://leetcode.com/problems/max-consecutive-ones-iii/?envType=problem-list-v2&envId=binary-search
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
  
        left = 0
        right = 0
        cur_k = k

        for right in nums:
            if right == 0:
                cur_k -= 1
            
            if cur_k < 0:
                if nums[left] == 0:
                    cur_k += 1
                left += 1
        return len(nums) - left 
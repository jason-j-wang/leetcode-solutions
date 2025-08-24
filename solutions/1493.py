#https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        deleted = False

        left = 0
        cur_len = 0

        for right in range(len(nums)):
            if nums[right]:
                cur_len += 1
                
            else:
                ans = max(ans, cur_len)
                if not deleted:
                    deleted = True
                    continue
                
                while left <= right:
                    if nums[left]:
                        cur_len -= 1
                        left += 1
                    else:
                        left += 1
                        break
                    
        ans = max(ans, cur_len)
        
        return ans if deleted else ans - 1
        
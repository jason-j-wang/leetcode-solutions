#https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/?envType=daily-question&envId=2025-10-31
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == -float('inf'):
                num = 0
            else:
                num = abs(num)

            if nums[num] < 0:
                ans.append(num)

            nums[num] = -abs(nums[num]) if nums[num] != 0 else -float('inf')
 
        return ans
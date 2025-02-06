#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = 0
        maj = 0
        for num in nums:
            if maj == 0:
                cur = num
            
            if cur == num:
                maj += 1
            else:
                maj -= 1
        return cur
#https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2025-05-17
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_ptr = 0
        right_ptr = len(nums)-1
        cur_ptr = 0

        while cur_ptr <= right_ptr:
            n = nums[cur_ptr]

            if n == 0:
                nums[left_ptr], nums[cur_ptr] = nums[cur_ptr], nums[left_ptr]
                left_ptr += 1
                cur_ptr += 1
            elif n == 1:
                cur_ptr += 1

            else:
                nums[right_ptr], nums[cur_ptr] = nums[cur_ptr], nums[right_ptr]
                right_ptr -= 1
        


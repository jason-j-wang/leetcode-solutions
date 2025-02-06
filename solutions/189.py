#https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate = k % len(nums)
        if rotate == 0:
            return
       
        start = 0
        cur = (start + rotate) % len(nums)
        min_seen = start + rotate
        #find the number of "groups"
        while cur != start:
            min_seen = min(min_seen, cur)
            cur = (cur + rotate) % len(nums)
        n = min_seen

        for i in range(n):
            cur_idx = (i + rotate) % len(nums)
            replaced = nums[i]

            while cur_idx != i:
                next_idx = (cur_idx + rotate) % len(nums)
                temp = nums[cur_idx]
                nums[cur_idx] = replaced
                replaced = temp
                cur_idx = next_idx
            
            #final swap
            nums[cur_idx] = replaced

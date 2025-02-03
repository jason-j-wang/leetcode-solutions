#https://leetcode.com/problems/find-if-array-can-be-sorted/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits = nums[0].bit_count()
        cur_max = nums[0]
        prev_max = -1

        for n in nums:
            b = n.bit_count()

            if b != bits:
                if n > cur_max:
                    bits = b
                    prev_max = cur_max
                    cur_max = n
                else:
                    return False
            elif n < prev_max:
                return False
            else:
                cur_max = max(n, cur_max)
        return True
        
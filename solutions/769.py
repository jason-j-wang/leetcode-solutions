#https://leetcode.com/problems/max-chunks-to-make-sorted/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_num = 9

        nums = [0] * (max_num + 1)
        partitions = 0
        min_ptr = 0
        max_ptr = 0
        
        for n in arr:
            max_ptr = max(n, max_ptr)
            nums[n] = 1

            if n == min_ptr:
                while nums[min_ptr] and min_ptr < max_ptr:
                    min_ptr += 1

            if min_ptr == max_ptr:
                partitions += 1
                max_ptr += 1
                min_ptr = max_ptr

        
        return partitions

            

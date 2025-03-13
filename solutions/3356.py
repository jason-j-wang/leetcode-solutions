#https://leetcode.com/problems/zero-array-transformation-ii/description/?envType=daily-question&envId=2025-03-13
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        prefix = [0 for i in range(len(nums) + 1)]
        cur_sum = 0
        k = 0
        for i in range(len(nums)):
            while cur_sum + prefix[i] < nums[i]:
                k += 1

                if k > len(queries):
                    return -1

                l, r, v = queries[k-1]

                if r >= i:
                    prefix[max(l, i)] += v
                    prefix[r + 1] -= v

            cur_sum += prefix[i]
        return k
   
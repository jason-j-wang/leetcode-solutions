#https://leetcode.com/problems/maximum-xor-for-each-query/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        max_num = 2 ** maximumBit - 1

        x = nums[0]
        for i in range(1, len(nums)):
            x ^= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            ans.append(max_num ^ x)
            x ^= nums[i]
        return ans
        
        
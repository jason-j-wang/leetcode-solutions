#https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/class Solution:
def maximumTripletValue(self, nums: List[int]) -> int:
    ans = 0
    i = 0
    ij = 0
    for k in range(len(nums)):
        ans = max(ans, ij * nums[k])
        ij = max(ij, i - nums[k])
        i = max(i, nums[k])
    return ans
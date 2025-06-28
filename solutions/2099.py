#https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/?envType=daily-question&envId=2025-06-28
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        idx = [i for i in range(len(nums))]

        idx.sort(reverse=True, key= lambda x: nums[x])
        idx = idx[0:k]
        idx.sort()

        ans = []
        for i in range(k):
            ans.append(nums[idx[i]])
        return ans
#https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/?envType=daily-question&envId=2025-06-24
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ks = []

        for i in range(len(nums)):
            if nums[i] == key:
                ks.append(i)

        if not ks:
            return []

        ptr = 0
        ans = []
        i = 0

        while i < len(nums):
            if abs(i - ks[ptr]) <= k:
                ans.append(i)
                i += 1
            else:
                if ks[ptr] < i and ptr < len(ks) - 1:
                    ptr += 1
                else:
                    i += 1
        return ans
                    

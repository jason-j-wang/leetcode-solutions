#https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=daily-question&envId=2025-06-30
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        keys = list(counts.keys())
        ans = 0
        
        for n in keys:
            if n + 1 in counts:
                if counts[n] + counts[n+1] > ans:
                    ans = counts[n] + counts[n+1] 
        return ans
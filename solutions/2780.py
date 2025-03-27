#https://leetcode.com/problems/minimum-index-of-a-valid-split/description/?envType=daily-question&envId=2025-03-27
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c = Counter(nums)
        length = len(nums)
        dom = -1
        dom_count = 0

        for n in c:
            if c[n] > dom_count:
                dom_count = c[n]
                dom = n
        
        count = 0

        for i in range(len(nums)):
            if nums[i] == dom:
                count += 1
            
            if count > i + 1 - count and (dom_count - count) * 2 > length - i - 1:
                return i
        return -1
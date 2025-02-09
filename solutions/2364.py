#https://leetcode.com/problems/count-number-of-bad-pairs/description/?envType=daily-question&envId=2025-02-09
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:   
        indices = defaultdict(int)
        bad_pairs = 0
        for j in range(len(nums)):
            diff = nums[j] - j
            good_pairs = indices[diff]

            bad_pairs += j - good_pairs

            indices[diff] += 1
        return bad_pairs


        


        

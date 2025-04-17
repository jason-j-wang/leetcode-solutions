#https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/?envType=daily-question&envId=2025-04-17
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        idx = defaultdict(list)
        ans = 0
        for i, n in enumerate(nums):
            for j in idx[n]:
                if i * j % k == 0:
                    ans += 1
            idx[n].append(i)
        return ans
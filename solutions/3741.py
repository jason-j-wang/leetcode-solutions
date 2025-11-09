#https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description/
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        loc = defaultdict(list)
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            loc[nums[i]].append(i)

        for num in loc:
            if len(loc[num]) < 3:
                continue

            idx = loc[num]

            for id in range(2, len(idx)):
                i = idx[id - 2]
                j = idx[id - 1]
                k = idx[id]
                ans = min(ans, abs(i - j) + abs(j - k) + abs(k - i))

        return ans if ans != float('inf') else -1
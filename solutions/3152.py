#https://leetcode.com/problems/special-array-ii/
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        count = 0

        for i in range(1, len(nums)):
            if nums[i-1] % 2 == nums[i] % 2:
                count += 1
            prefix.append(count)

        ans = []

        for q in queries:
            if prefix[q[0]] != prefix[q[1]]:
                ans.append(False)
            else:
                ans.append(True)
        return ans
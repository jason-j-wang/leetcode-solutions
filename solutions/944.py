#https://leetcode.com/problems/delete-columns-to-make-sorted/?envType=daily-question&envId=2025-12-20
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    ans += 1
                    break
        return ans

#https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2025-02-20
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            bit = nums[i][i]
            ans.append("1" if bit == "0" else "0")
        return "".join(ans)

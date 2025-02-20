#https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2025-02-20
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        _, ans = self.build(s, "")
        return ans


    def build(self, nums, cur):
        if len(cur) == len(nums) and cur not in nums:
            return True, cur

        if len(cur) == len(nums):
            return False, ""

        bits = ["0", "1"]

        for b in bits:
            valid, string = self.build(nums, cur + b)
            if valid:
                return True, string
        return False, ""

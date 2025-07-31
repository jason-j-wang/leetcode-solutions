#https://leetcode.com/problems/bitwise-ors-of-subarrays/solutions/165881/c-java-python-o-30n/?envType=daily-question&envId=2025-07-31
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
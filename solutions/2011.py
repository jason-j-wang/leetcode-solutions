#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/?envType=daily-question&envId=2025-10-20
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op[0] == "+" or op[-1] == "+":
                x += 1
            else:
                x -= 1
        return x
#https://leetcode.com/problems/calculate-score-after-performing-instructions/description/
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        visited = set()
        score = 0
        i = 0
        while i < len(values) and i >= 0:
            if i in visited:
                return score
            visited.add(i)

            if instructions[i] == "add":
                score += values[i]
                i += 1
            else:
                i = i + values[i]

        return score
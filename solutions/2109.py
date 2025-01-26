#https://leetcode.com/problems/adding-spaces-to-a-string/?envType=daily-question&envId=2025-01-26
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        segments = []
        start = 0

        for space in spaces:
            segments.append(s[start:space])
            start = space

        segments.append(s[start:])

        return " ".join(segments)

        
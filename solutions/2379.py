#https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/?envType=daily-question&envId=2025-03-08
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0

        left = 0
        right = k-1
        for i in range(k):
            if blocks[i] == "W":
                whites += 1

        ans = whites

        while right < len(blocks)-1:
            ans = min(ans, whites)

            if blocks[left] == "W":
                whites -= 1
            
            if blocks[right + 1] == "W":
                whites += 1

            left += 1
            right += 1
        return min(ans, whites)

            
            
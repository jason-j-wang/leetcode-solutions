#https://leetcode.com/problems/fruits-into-baskets-ii/description/
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False for i in range(len(baskets))]
        ans = 0
        for f in fruits:
            placed = False
            for i in range(len(baskets)):
                
                if not used[i] and baskets[i] >= f:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                ans += 1
        return ans
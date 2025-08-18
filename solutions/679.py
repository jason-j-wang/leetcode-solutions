#https://leetcode.com/problems/24-game/description/?envType=daily-question&envId=2025-08-18
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return math.isclose(cards[0], 24)

        for i in range(len(cards)):
            for j in range(len(cards)):
                if i != j:
                    arr = [cards[i] + cards[j]] + [cards[k] for k in range(len(cards)) if k != i and k != j]
                    if self.judgePoint24(arr):
                        return True

                    arr = [cards[i] - cards[j]] + [cards[k] for k in range(len(cards)) if k != i and k != j]
                    if self.judgePoint24(arr):
                        return True

                    arr = [cards[i] * cards[j]] + [cards[k] for k in range(len(cards)) if k != i and k != j]
                    if self.judgePoint24(arr):
                        return True

                    if cards[j]:
                        arr = [cards[i] / cards[j]] + [cards[k] for k in range(len(cards)) if k != i and k != j]
                        if self.judgePoint24(arr):
                            return True
        return False
#https://leetcode.com/problems/eat-pizzas/
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        weight = 0
        days = len(pizzas) // 4

        start = len(pizzas) - 1

        odds = days // 2
        even = odds
        if days % 2 == 1:
            odds += 1
            
        for i in range(odds):
            weight += pizzas[start]
            start -= 1

        for i in range(even):
            weight += pizzas[start-1]
            start -= 2
        return weight
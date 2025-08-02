#https://leetcode.com/problems/rearranging-fruits/description/?envType=daily-question&envId=2025-08-02
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1 = defaultdict(int, Counter(basket1))
        c2 = defaultdict(int, Counter(basket2))

        swaps = []

        from1 = 0
        from2 = 0

        min_num = float('inf')

        for cost in c1:
            if (c1[cost] + c2[cost]) % 2 != 0:
                return -1

            if cost < min_num:
                min_num = cost

            diff = c1[cost] - c2[cost]
            diff //= 2
            if diff > 0:
                from1 += diff
                for _ in range(diff):
                    swaps.append(cost)

        for cost in c2:
            if (c1[cost] + c2[cost]) % 2 != 0:
                return -1

            if cost < min_num:
                min_num = cost

            diff = c2[cost] - c1[cost]
            diff //= 2
            if diff > 0:
                from2 += diff
                for _ in range(diff):
                    swaps.append(cost)
        if from1 != from2:
            return -1

        ans = 0
        swaps.sort()
    
        for i in range(from1):
            cost = swaps[i]

            if cost < min_num * 2:
                ans += cost
            else:
                ans += min_num * 2
        return ans
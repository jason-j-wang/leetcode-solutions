#https://leetcode.com/problems/candy/submissions/1651242679/?envType=daily-question&envId=2025-06-02
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = 0

        candies = [1 for _ in range(len(ratings))]
        ans = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i] + 1, candies[i-1])
            ans += candies[i-1]
        return ans + candies[-1]
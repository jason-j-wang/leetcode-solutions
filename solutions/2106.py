#https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description/?envType=daily-question&envId=2025-08-03
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans = 0
        left = 0
        right = 0
        ans = 0
        cur_fruits = 0

        n = len(fruits)

        while right < n:
            cur_fruits += fruits[right][1]

            while left <= right and self.num_steps(fruits, startPos, left, right) > k:
                cur_fruits -= fruits[left][1]
                left += 1

            if cur_fruits > ans:
                ans = cur_fruits

            right += 1
        return ans

    def num_steps(self, fruits, start, left, right):
        if start >= fruits[right][0]:
            return start - fruits[left][0]

        if start <= fruits[left][0]:
            return fruits[right][0] - start

        return min((start - fruits[left][0]) * 2 + fruits[right][0] - start, 
        (fruits[right][0] - start) * 2 + start - fruits[left][0])

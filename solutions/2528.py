#https://leetcode.com/problems/maximize-the-minimum-powered-city/description/?envType=daily-question&envId=2025-11-07
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0 for _ in range(n)]
        left, right = 0, r - 1

        cur_pow = 0
        for i in range(r):
            cur_pow += stations[i]

        for i in range(n):
            right += 1
            if right < n:
                cur_pow += stations[right]

            if right - left > 2 * r:
                cur_pow -= stations[left]
                left += 1

            power[i] = cur_pow
        

        left = min(power)
        right = max(power) + k

        while left <= right:
            mid = (left + right) // 2
            if self.validate(power, r, k, mid, n):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


        
    def validate(self, power, r, k, target, n):
        remove = [0 for _ in range(n + 1)]
        cur_towers = 0

        for i in range(n):
            cur_towers -= remove[i]
            p = power[i] + cur_towers

            if p < target:
                needed = target - p

                if k < needed:
                    return False

                k -= needed
                cur_towers += needed
                remove[min(n, i + 2 * r + 1)] += needed

        return True

#https://leetcode.com/problems/closest-prime-numbers-in-range/?envType=daily-question&envId=2025-03-07
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = self.sieve(right)

        primes = [i for i in range(left, right + 1) if sieve[i]]

        if len(primes) < 2:
            return [-1, -1]

        diff = float("inf")
        ans = [-1, -1]

        for i in range(1, len(primes)):
            d = primes[i] - primes[i-1]
            if d < diff:
                diff = d
                ans = [primes[i-1], primes[i]]
        return ans

    def sieve(self, limit):
        s = [True for _ in range(limit + 1)]
        s[0] = False
        s[1] = False

        for i in range(2, int(limit ** 0.5) + 1):
            if s[i]:
                for m in range(i * i, limit + 1, i):
                    s[m] = False
        return s

    
        
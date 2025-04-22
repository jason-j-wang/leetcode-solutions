#https://leetcode.com/problems/count-the-number-of-ideal-arrays/description/?envType=daily-question&envId=2025-04-22
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10 ** 9 + 7
        lim = 10 ** 4 + 10
        max_p = 15

        sieve = [0 for i in range(lim)]

        for i in range(2, lim):
            if sieve[i] == 0:
                for j in range(i, lim, i):
                    sieve[j] = i

        prime_factors = [[] for i in range(lim)]

        for i in range(2, lim):
            num = i

            while num > 1:
                prime = sieve[num]
                count = 0
                while num % prime == 0:
                    num //= prime
                    count += 1

                prime_factors[i].append(count)

        combs = [[0 for i in range(max_p + 1)] for i in range(lim + max_p)]
        combs[0][0] = 1

        for i in range(1, lim + max_p):
            combs[i][0] = 1
            for j in range(1, min(i, max_p)+1):
                combs[i][j] = (combs[i - 1][j] + combs[i - 1][j - 1]) % mod


        ans = 0

        for i in range(1, maxValue + 1):
            cur = 1
            for prime in prime_factors[i]:
                cur = cur * combs[n + prime - 1][prime] % mod
            ans = (ans + cur) % mod
        return ans


        

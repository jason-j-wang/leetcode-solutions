#https://leetcode.com/problems/find-the-count-of-good-integers/description/?envType=daily-question&envId=2025-04-12
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        seen = set()
        digits = 10 ** ((n - 1) // 2)
        odd = n % 2 == 1

        for i in range(digits, digits * 10):
            s = str(i)
            s += s[::-1][odd:]
            palindrome = int(s)

            if palindrome % k == 0:
                sort_str = "".join(sorted(s))
                seen.add(sort_str)

        fact = [factorial(i) for i in range(n+1)]
        ans = 0

        for s in seen:
            count = [0 for i in range(10)]
            for c in s:
                count[int(c)] += 1
            total = (n - count[0]) * fact[n-1]
            for cnt in count:
                total //= fact[cnt]
            ans += total
        return ans
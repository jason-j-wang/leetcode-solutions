#https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/?envType=daily-question&envId=2025-05-27
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        allSum = n * (n + 1) // 2
        numNumbersDivisibleByM = n // m
        sumOfDivs = m * (numNumbersDivisibleByM * (numNumbersDivisibleByM + 1) // 2)
        
        return (allSum - sumOfDivs * 2)
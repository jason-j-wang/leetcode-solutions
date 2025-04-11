#https://leetcode.com/problems/count-symmetric-integers/description/?envType=daily-question&envId=2025-04-11
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            n = len(str(i))
            if n % 2 == 0:
                div = 10 ** (n // 2)

                left = i // div
                right = i % div

                left_sum = sum([int(j) for j in str(left)])
                right_sum = sum([int(j) for j in str(right)])

                if left_sum == right_sum:
                    ans +=1 
        return ans

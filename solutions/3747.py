#https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/description/
class Solution:
    def countDistinct(self, n: int) -> int:
        start = 1

        ans = 0

        while 10 ** start < n:
            ans += 9 ** start
            start += 1

        num_digits = start

        temp = n
        temp_ans = 0

        #eg if 2345, doing 1xxx
        i = num_digits - 1
        div = 10 ** (num_digits - 1)
        while temp > 0:
            first_digit = temp // div
            if first_digit == 0:
                break

            temp_ans += (first_digit - 1) * 9 ** i
            i -= 1
            temp %= div
            div //= 10
        ans += temp_ans

        if str(n).count("0") == 0:
            ans += 1

        return ans
            
        
#https://leetcode.com/problems/sum-of-k-mirror-numbers/description/?envType=daily-question&envId=2025-06-23
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        start = 1
        ans = 0

        count = 0

        while count < n:
            end = start * 10

            for even in range(2):
                for i in range(start, end):
                    if count == n:
                        break

                    num = i

                    append_part = i // 10 if even == 0 else i

                    while append_part:
                        num = num * 10 + append_part % 10
                        append_part //= 10
                    
                    if self.valid(num, k):
                        count += 1
                        ans += num
            start = end
        return ans  

    def valid(self, x, k):
        digit = list()
        while x:
            digit.append(x % k)
            x //= k
        return digit == digit[::-1]
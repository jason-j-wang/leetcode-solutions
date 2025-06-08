#https://leetcode.com/problems/lexicographical-numbers/description/?envType=daily-question&envId=2025-06-08
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        num = 1
        
        for i in range(n):
            ans.append(num)

            if num * 10 <= n:
                num *= 10

            else:
                while num % 10 == 9 or num >= n:
                    num //= 10
                num += 1
        return ans
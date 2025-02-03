#https://leetcode.com/problems/maximum-swap/?envType=daily-question&envId=2025-02-03
class Solution:
    def maximumSwap(self, num: int) -> int:
        l = []
        temp = num
        while (temp != 0):
            l.append(temp % 10)
            temp = temp // 10
        
        for i in range(len(l) - 1, -1, -1):
            if l[i] != 9:
                idx = -1
                n = -1
                for j in range(i - 1, -1, -1):
                    if l[j] >= n:
                        idx = j
                        n = l[j]
                if n > l[i]:
                    temp = l[i]
                    l[i] = n
                    l[idx] = temp
                    break
        ans = 0
        for i in range(len(l)):
            ans += l[i] * (10 ** i)
        return ans
#https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/?envType=daily-question&envId=2025-05-13
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod= 10 ** 9 + 7
        count = [0 for i in range(26)]

        for c in s:
            count[ord(c) - ord('a')] += 1

        for i in range(t):
            next = [0 for _ in range(26)]

            for j in range(1, 26):
                next[j] = count[j-1]

            next[0] = count[25]
            next[1] = (count[0] + count[25]) % mod
            count = next

       
        return sum(count) % mod
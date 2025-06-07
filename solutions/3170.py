#https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/?envType=daily-question&envId=2025-06-07
class Solution:
    def clearStars(self, s: str) -> str:
        removed = [False for i in range(len(s))]

        heap = []

        for i in range(len(s)):
            if s[i] == "*":
                _, j = heapq.heappop(heap)
                removed[i] = True
                removed[-j] = True
            else:
                heapq.heappush(heap, (s[i], -i))

        ans = ""
        for i in range(len(s)):
            if not removed[i]:
                ans += s[i]
        return ans
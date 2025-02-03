#https://leetcode.com/problems/longest-happy-string/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))

        if b > 0:
            heapq.heappush(heap, (-b, "b"))

        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        ans = ""

        while heap:
            num, char = heapq.heappop(heap)
            num = -num
            if len(ans) >= 2 and ans[-1] == char and ans[-2] == char:
                if not heap:
                    break
                temp_num, temp_char = heapq.heappop(heap)
                ans += temp_char
                if temp_num + 1 < 0:
                    heapq.heappush(heap, (temp_num + 1, temp_char))
                heapq.heappush(heap, (-num, char))
            else:
                num -= 1
                ans += char
                if num > 0:
                    heapq.heappush(heap, (-num, char))
        return ans




        
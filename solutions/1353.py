#https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/?envType=daily-question&envId=2025-07-07
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        max_day = max(e[1] for e in events)
        n = len(events)
        events.sort()
        ans = 0
        cur_idx = 0
        q = []

        for i in range(1, max_day + 1):
            while cur_idx < n and events[cur_idx][0]  <= i:
                heapq.heappush(q, events[cur_idx][1])
                cur_idx += 1
            while q and q[0] < i:
                heapq.heappop(q)
            if q:
                heapq.heappop(q)
                ans += 1
        return ans


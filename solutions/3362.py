#https://leetcode.com/problems/zero-array-transformation-iii/description/?envType=daily-question&envId=2025-05-22
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        q = []
        prefix = [0 for _ in range(len(nums) + 1)]

        queries_ptr = 0
        cur = 0

        for i, n in enumerate(nums):
            cur += prefix[i]

            while queries_ptr < len(queries) and queries[queries_ptr][0] == i:
                heapq.heappush(q, -queries[queries_ptr][1])
                queries_ptr += 1
            
            while cur < n and q and -q[0] >= i:
                cur += 1
                end = heapq.heappop(q)
                prefix[-end + 1] -= 1

            if cur < n:
                return -1
        return len(q)
#https://leetcode.com/problems/apply-operations-to-maximize-score/description/?envType=daily-question&envId=2025-03-29
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mem = {}
        n = len(nums)
        scores = [0 for _ in range(n)]

        for i in range(n):
            num = nums[i]
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    scores[i] += 1
                while num % j == 0:
                    num //= j
            if num > 1:
                scores[i] += 1

        next_dom = [n for _ in range(n)]
        prev_dom = [-1 for _ in range(n)]
        stack = []

        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                popped = stack.pop()
                next_dom[popped] = i

            if stack:
                prev_dom[i] = stack[-1]

            stack.append(i)

        subs = [0 for _ in range(n)]

        for i in range(n):
            subs[i] = (next_dom[i] - i) * (i - prev_dom[i])

        q = []
        for i in range(n):
            heapq.heappush(q, (-nums[i], i))

        ans = 1

        while k > 0:
            num, i = heapq.heappop(q)
            num = -num

            times = min(subs[i], k)
            k -= times
            while times > 0:
                if times % 2 == 1:
                    ans = (ans * num) % (10 ** 9 + 7)

                num = (num ** 2) % (10 ** 9 + 7)
                times //= 2

        return ans
#https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        if len(quantities) == 1:
            return (quantities[0] + n - 1)//n

        q = []
        total_div = len(quantities)

        for qu in quantities:
            heapq.heappush(q, [-qu, -qu, 1])


        
        while total_div < n:
            cur_num, original_num, div = heapq.heappop(q)
            cur_num = -cur_num
            original_num = -original_num

            next_cur, next_orig, next_div = q[0]
            next_cur = -next_cur
            next_orig = -next_orig

            while total_div < n and ((original_num + div - 1) // div) >= ((next_orig + next_div - 1) // next_div):
                #print(original_num, ((cur_num + div - 1) // div), ((next_cur + next_div - 1) // next_div))
                total_div += 1
                div += 1
            
            num = -((original_num + div - 1) // div)
            heapq.heappush(q, [num, -original_num, div])

        #print(q)
        ans = heapq.heappop(q)
        return -ans[0]
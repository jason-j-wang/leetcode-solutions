#https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/description/
class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        
        prefix = [0 for _ in range(n)]
        pd = defaultdict(int)
        ans = 0
        cur = 0
        for i in range(n):
            num = capacity[i]

            if i > 1:     
                target = prefix[i-1] - num
                ans += pd[target, num]

                if num == 0 and capacity[i-1] == 0:
                    ans -= 1
                
            cur += num
            prefix[i] = cur

            pd[(cur, num)] += 1

        return ans
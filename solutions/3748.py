#https://leetcode.com/problems/count-stable-subarrays/description/
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prev = -1

        n = len(nums)
        total = 0
        left = 0
        prefix = [0 for _ in range(n)]
        num_invs = [0 for _ in range(n)]
        next_inv = [-1 for _ in range(n)]
        prev_inv = [-1 for _ in range(n)]

        #simultaneously calc prefix and previous inversion for each index
        pi = -1
        for i, num in enumerate(nums):
            #inversion
            if num < prev:
                num_invs[i] += 1
                length = i - left
                total += length * (length + 1) // 2
                for j in range(left, i):
                    prefix[j] = total
                left = i
                    
            if i > 0:
                num_invs[i] += num_invs[i-1]
            prev = num

            if num_invs[i] != num_invs[i-1]:
                pi = i - 1
            prev_inv[i] = pi
            
        length = n - left
        total += length * (length + 1) // 2
        for j in range(left, n):
            prefix[j] = total

        # next inversion for each index
        next = -1
        for i in range(n - 2, -1, -1):
            if num_invs[i] != num_invs[i+1]:
                next = i + 1
            next_inv[i] = next

        ans = [0 for _ in range(len(queries))]

        for i, (l, r) in enumerate(queries):
            if num_invs[l] == num_invs[r]:
                length = r - l + 1
                ans[i] = length * (length + 1) // 2
            else:
                left_next = next_inv[l]
                right_prev = prev_inv[r]
                base = max(0, prefix[right_prev] - prefix[l])
                
                left_length = left_next - l
                base += left_length * (left_length + 1) // 2

                right_prev = prev_inv[r]
                right_length = r - right_prev
                base += right_length * (right_length + 1) // 2
                ans[i] = base
                
        return ans
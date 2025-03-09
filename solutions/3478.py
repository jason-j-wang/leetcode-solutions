#https://leetcode.com/problems/choose-k-elements-with-maximum-sum/description/
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1 = []
        n2 = []
        ans = [0 for i in range(len(nums1))]

        for i in range(len(nums1)):
            n1.append((nums1[i], i))
            n2.append((nums2[i], i))

        n1.sort(reverse=True)
        n2.sort(reverse=True)

        cur_sum = 0
        ptr = 0

        used = []

        count = 0
        for i in range(len(n1)):
            
            val, idx = n1[i]

            while used and -used[0][0] >= nums1[idx]:
                count -= 1
                cur_sum -= nums2[used[0][1]]
                heapq.heappop(used)

            # add new ones
            while ptr < len(n2) and count < k:
                new_val, new_idx = n2[ptr]
                if nums1[new_idx] < val:     
                    heapq.heappush(used, (-nums1[new_idx], new_idx))
                    cur_sum += new_val
                    count += 1
                ptr += 1

            ans[idx] = cur_sum
        return ans
                
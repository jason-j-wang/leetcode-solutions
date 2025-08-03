#https://leetcode.com/problems/trionic-array-ii/description/
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:

        start = 0
        n = len(nums)
        ans = -float('inf')

        while start < n - 3:
            p = -1
            q = -1
            total_sum = 0

            finished_for = True
            #get subarray if exists starting at start
            for i in range(start, n):

                #first length
                if p == -1 and q == -1:
                    if i == start or nums[i] > nums[i-1]:
                        total_sum += nums[i]
                    elif nums[i] == nums[i-1]:
                        start = i
                        finished_for = False
                        break
                    else:
                        p = i - 1

                        if p == start:
                            start = i
                            finished_for = False
                            break

                        cur_reverse = nums[p]
                        for j in range(p - 1, start-1, -1):
                            cur_reverse += nums[j]
                            total_sum = max(total_sum, cur_reverse)

                        
                        total_sum += nums[i]

                #second length
                elif p != -1 and q == -1:
                    if nums[i] < nums[i-1]:
                        total_sum += nums[i]
                    elif nums[i] == nums[i-1]:
                        start = i
                        finished_for = False
                        break
                    else:
                        q = i - 1
                        if q == p:
                            start = i
                            finished_for = False
                            break
                        total_sum += nums[i]
                        ans = max(ans, total_sum)

                #third length
                else:
                    if nums[i] > nums[i-1]:
                        total_sum += nums[i]
                        ans = max(ans, total_sum)
                    elif nums[i] == nums[i-1]:
                        start = i
                        finished_for = False
                        break
                    else:
                        start = q
                        finished_for = False
                        break
            if finished_for:
                return ans
        return ans
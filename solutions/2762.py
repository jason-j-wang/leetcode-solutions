#https://leetcode.com/problems/continuous-subarrays/?envType=daily-question&envId=2025-01-26
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        right = 0
        largest = -float("infinity")
        smallest = float("infinity")
        idx = defaultdict(int)

        contains_prev = False
        total = 0

        while left <= right and right < len(nums):

            idx[nums[right]] = right
            largest = max(largest, nums[right])
            smallest = min(smallest, nums[right])

            if largest - smallest > 2:
                length = right - left
                if not contains_prev:
                    total += length * (length + 1) // 2

                if abs(nums[right] - nums[right - 1]) > 2:
                    contains_prev = False
                    left = right
                    smallest = nums[right]
                    largest = nums[right]
                else:
                    contains_prev = True
                    left, smallest, largest = self.findNext(smallest, largest, left, right, idx, nums[right], nums)

            
            if contains_prev:
                total += right - left + 1

            right += 1

        if not contains_prev:
            length = right - left
            total += length * (length + 1) // 2

        return total
    
    def findNext(self, smallest, largest, left, right, idx, num, nums):
        s = smallest
        l = largest
        left = left
        if largest == num:
            
            left = idx[smallest] + 1
            s = nums[left] if (nums[left] == num - 2 or idx[num-2] < left) else num -1

        else:
            
            left = idx[largest] + 1
            l = nums[left] if (nums[left] == num + 2 or idx[num+2] < left) else num +1
        return left, s, l
        
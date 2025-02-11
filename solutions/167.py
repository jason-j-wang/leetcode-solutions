#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum == target:
                return [left + 1, right+1]
            else:
                right -= 1
        return []
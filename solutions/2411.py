#https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description/?envType=daily-question&envId=2025-07-29
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]

        cur = 0
        right = n - 1

        bits = [0 for i in range(max(nums).bit_length())]

        for i in range(n - 1, -1, -1):
            cur |= nums[i]
            valid = True

            exp = nums[i].bit_length()
            num = nums[i]
            for e in range(exp - 1, -1, -1):
                if 2 ** e <=  num:
                    bits[e] += 1
                    num -= 2 ** e

            while right > i and valid:
                bit_copy = bits.copy()
                exp = nums[right].bit_length()
                right_num= nums[right]

                for e in range(exp - 1, -1, -1):
                    if 2 ** e <= right_num:
                        right_num -= 2 ** e
                        bit_copy[e] -= 1

                        if bit_copy[e] == 0:
                            valid = False
                            break
                if valid:
                    bits = bit_copy
                    right -= 1
            ans[i] = right - i + 1
        return ans

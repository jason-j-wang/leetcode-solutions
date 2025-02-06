#https://leetcode.com/problems/tuple-with-same-product/description/?envType=daily-question&envId=2025-02-06
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count[nums[i] * nums[j]] += 1
        
        ans = 0
        for product in count:
            if count[product] > 1:
                n = count[product]
                ans += 8 * (factorial(n) / (factorial(n-2) * 2))
        return int(ans)

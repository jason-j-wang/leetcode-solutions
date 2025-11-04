#https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/?envType=daily-question&envId=2025-11-04
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        count = None
        for i in range(n - k + 1):
            if count is None:
                count = Counter(nums[:k])
                count = defaultdict(int, count)
            else:
                b = nums[i-1]
                count[b] -= 1

                num = nums[i + k - 1]
                count[num] += 1

            s = 0
            arr = [(count[i], i) for i in count]
            arr.sort(reverse=True)
            for j in range(min(x, len(arr))):
                c, n = arr[j]
                s += c * n
            ans.append(s)
        return ans
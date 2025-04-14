#https://leetcode.com/problems/count-good-triplets/description/?envType=daily-question&envId=2025-04-14
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        prefix = [0 for i in range(1001)]

        for j in range(n):
            for k in range(j+1, n):
                if abs(arr[j] - arr[k]) <= b:
                    leftj, rightj = arr[j] - a, arr[j] + a
                    leftk, rightk = arr[k] - c, arr[k] + c
                    left = max(0, leftj, leftk)
                    right = min(1000, rightj, rightk)

                    if left <= right:
                        ans += prefix[right] if left == 0 else prefix[right] - prefix[left-1]
            for k in range(arr[j], 1001):
                prefix[k] += 1
        return ans
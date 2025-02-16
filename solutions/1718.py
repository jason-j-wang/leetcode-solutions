#https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/?envType=daily-question&envId=2025-02-16
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [-1 for i in range(n * 2 -1)]

        used = [False for i in range(n)]

        nums = [i for i in range(n, 0, -1)]

        self.solve(seq, 0, nums, used, n)
        return seq

    def solve(self, seq, cur_idx, nums, used, n):
        if n == 0:
            return True

        if cur_idx >= len(seq):
            return False

        if seq[cur_idx] != -1:
            return self.solve(seq, cur_idx + 1, nums, used, n)

        for i in range(len(nums)):
            if nums[i] == 1 and not used[i]:
                seq[cur_idx] = 1
                used[i] = True
                if self.solve(seq, cur_idx + 1, nums, used, n - 1):
                    return True
                seq[cur_idx] = -1
                used[i] = False
            elif not used[i] and cur_idx + nums[i] < len(seq) and seq[cur_idx + nums[i]] == -1:
                used[i] = True
                seq[cur_idx] = nums[i]
                seq[cur_idx+nums[i]] = nums[i]
                if self.solve(seq, cur_idx + 1, nums, used, n - 1):
                    return True
                used[i] = False
                seq[cur_idx] = -1
                seq[cur_idx+nums[i]] = -1
        return False


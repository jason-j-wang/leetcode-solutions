#https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description/?envType=daily-question&envId=2025-05-01
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        n = len(tasks)
        m = len(workers)

        left = 0
        right = min(n, m)
        ans= 0

        while left <= right:
            mid = right - (right - left) // 2

            if self.validate(tasks, workers[m - mid:], mid, pills, strength):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


    def validate(self, tasks, workers, num, pills, strength):
        task_map = tasks[:num][::-1]

        for t in task_map:
            if t <= workers[-1]:
                workers.pop()

            else:
                if pills == 0:
                    return False

                i = bisect.bisect_left(workers, t - strength)
                if i == len(workers):
                    return False

                pills -= 1
                workers.pop(i)
        return True
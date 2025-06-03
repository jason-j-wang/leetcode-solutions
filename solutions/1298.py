#https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/?envType=daily-question&envId=2025-06-03
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque()
        ans = 0
        n = len(status)
        visited = [False for _ in range(n)]
        has_box = [False for _ in range(n)]

        for box in initialBoxes:
            has_box[box] = True
            if status[box] == 1:
                q.append(box)
                visited[box] = True
                ans += candies[box]        

        while q:
            box = q.popleft()

            for key in keys[box]:
                status[key] = 1
                if not visited[key] and has_box[key]:
                    q.append(key)
                    visited[key] = True
                    ans += candies[key]

            for nested_box in containedBoxes[box]:
                has_box[nested_box] = True
                if not visited[nested_box] and status[nested_box] == 1:
                    q.append(nested_box)
                    visited[nested_box] = True
                    ans += candies[nested_box]

        return ans
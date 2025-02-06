#https://leetcode.com/problems/course-schedule/?envType=problem-list-v2&envId=depth-first-search
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        visited = [False] * numCourses
        

        for p in prerequisites:
            adj[p[1]].append(p[0])

        # 0: unvisited course
        # 1: course that has been visited in a previous dfs call
        # -1: course that has been visited in the current dfs call
        visited = [0] * numCourses

        for n in range(numCourses):
            
            if not self.dfs(n, adj, visited):
                return False
        return True

    def dfs(self, cur, adj, visited):
        if visited[cur] == 1:
            return True

        if visited[cur] == -1:
            return False

        visited[cur] = -1

        for n in adj[cur]:
           
            if not self.dfs(n, adj, visited):
                return False

        visited[cur] = 1
        return True
#https://leetcode.com/problems/course-schedule-ii/description/?envType=problem-list-v2&envId=topological-sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        visited = [False for i in range(numCourses)]
        adj = [[] for i in range(numCourses)]

        in_degree = [0 for i in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        print(queue)
        while queue:
            course = queue.popleft()
            if visited[course]:
                return []

            order.append(course)
            visited[course] = True

            for next_course in adj[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []



        

        
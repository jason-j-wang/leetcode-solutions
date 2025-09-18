#https://leetcode.com/problems/design-task-manager/description/?envType=daily-question&envId=2025-09-18
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_ids = set()
        self.pq = []
        self.pmap = {}

        for u, t, p in tasks:
            self.add(u, t, p)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.pmap[taskId] = [priority, userId, False]
        self.task_ids.add(taskId)
        heapq.heappush(self.pq, [-priority, -taskId, userId])
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.pmap[taskId][0] = newPriority
        userId = self.pmap[taskId][1]
        heapq.heappush(self.pq, [-newPriority, -taskId, userId])
        
    def rmv(self, taskId: int) -> None:
        self.task_ids.remove(taskId)

    def execTop(self) -> int:
        if not self.pq:
            return -1

        while self.pq:
            p, t, u = heapq.heappop(self.pq)
            p = -p
            t = -t

            if self.pmap[t][0] == p and t in self.task_ids and self.pmap[t][1] == u and not self.pmap[t][2]:
                self.pmap[t][2] = True
                return u

        return -1




# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
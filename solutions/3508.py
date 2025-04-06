#https://leetcode.com/problems/implement-router/description/
class Router:

    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packets = deque()
        self.seen = set()
        self.dests = defaultdict(deque)
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        tuple = (source, destination, timestamp)
        if tuple in self.seen:
            return False
        if len(self.packets) == self.memory_limit:
            removed = self.packets.popleft()
            self.dests[removed[1]].popleft()
            self.seen.remove(removed)
        self.packets.append(tuple)
        self.seen.add(tuple)
        self.dests[destination].append(tuple)
        return True
            

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []

        removed = self.packets.popleft()
        self.seen.remove(removed)
        s, d, t = removed
        self.dests[d].popleft()
        return [s, d, t]
      

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.dests[destination]
        left = 0
        right = len(arr) - 1
        bottom = -1
        top = -1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][2] >= startTime:
                bottom = mid
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][2] <= endTime:
                top = mid
                left = mid + 1
            else:
                right = mid - 1

        return top - bottom + 1 if (top != -1 and bottom != -1) else 0
        

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
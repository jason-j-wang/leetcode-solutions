#https://leetcode.com/problems/lru-cache/description/
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.least_recent = ListNode(-1, -1)
        self.most_recent = ListNode(-1, -1)
        self.key_map = {}
        self.capacity = capacity
        self.cur_capacity = 0
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent
        

    def get(self, key: int) -> int:
        if key in self.key_map and self.key_map[key] != None:
            self.remove(self.key_map[key])
            self.insert(self.key_map[key])
            return self.key_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists in cache
        if key in self.key_map and self.key_map[key] != None:
            self.remove(self.key_map[key])
        elif self.cur_capacity < self.capacity:
            self.cur_capacity += 1
        else:
            old_key = self.least_recent.next.key
            self.remove(self.least_recent.next)
            self.key_map[old_key] = None

        new_node = ListNode(key, value)
        self.key_map[key] = new_node
        self.insert(new_node)


    def insert(self, node):
        prev, next = self.most_recent.prev, self.most_recent
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
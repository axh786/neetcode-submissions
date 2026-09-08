class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map the key to node

        self.left, self.right = Node(0, 0), Node(0, 0) # dummy nodes that bookmark and tell us whats mru & lru
        self.left.next = self.right # connected to one another, when inserting it gets put in the middle
        self.right.prev = self.left

    def remove(self, node): # remove from list, ptr function
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    
    def insert(self, node: int): # insert at right ptr function
        prv, nxt = self.right.prev, self.right

        prv.next = node
        node.prev = prv

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity: # delete the LRU from the cache
            lru = self.left.next # always the LRU
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
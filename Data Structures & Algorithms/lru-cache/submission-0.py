class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            curnode = self.cache[key]
            self.remove(curnode)
            self.insert(curnode)
            return curnode.val
        else:
            return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        newnode = self.insert(Node(key, value))    
        self.cache[key] = newnode

        if len(self.cache)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev
        node.prev.next = node
        self.right.prev = node    

        return node    
        

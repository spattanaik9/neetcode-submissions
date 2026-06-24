class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size

    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev, node.next = None, None
        self.size -= 1

    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node    

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfuCnt = 0
        self.nodeMap = {} #map key -> node
        #map frequency -> linkedlist of node (stored in lru fashion)
        self.listMap = defaultdict(LinkedList)
        
    def counter(self, node):
        #move this node from freq to freq+1 map
        
        cnt = node.freq
        self.listMap[cnt].pop(node)

        node.freq += 1
        self.listMap[cnt+1].pushRight(node)

        #check if no elements left in current frequency list, increase the least freq cnt
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt = cnt + 1


    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.val    
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 

        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return

        if len(self.nodeMap) == self.capacity:
            node = self.listMap[self.lfuCnt].popLeft()
            self.nodeMap.pop(node.key)

        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.listMap[1].pushRight(node)
        self.lfuCnt = 1            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
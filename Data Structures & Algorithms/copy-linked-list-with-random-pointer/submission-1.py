"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # dictionary to store old -> new mapping
        mapping = {}
        curnode = head
        while curnode:
            newnode = Node(curnode.val)
            mapping[curnode] = newnode
            curnode = curnode.next

        curnode = head
        while curnode:
            newnode = mapping[curnode]
            newnode.next = mapping[curnode.next] if curnode.next else None
            newnode.random = mapping[curnode.random] if curnode.random else None
            curnode = curnode.next

        return mapping[head]        

        
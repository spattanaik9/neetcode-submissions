# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        prev = None
        while cur:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode

        return prev    





        
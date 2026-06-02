# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grp_prev = dummy
        
        while True:
            kth = self.getKth(grp_prev, k)
            if not kth:
                break

            # position 0 node, and position k+1 node preserve them
            grp_nxt = kth.next  

            # reverse the group
            head, tail = self.reverseGroup(grp_prev.next, k)
            # print(head.val, tail.val)

            # point the prev pointer to the start of reversed group , and point the kth next to the k+1 preserved 
            grp_prev.next = head
            tail.next = grp_nxt
            grp_prev = tail
              
        return dummy.next
            
    def getKth(self, node, k):
        while node and k>0:
            node = node.next
            k -= 1
        return node       

    def reverseGroup(self, cur, k):
        temp = cur
        
        prev = None
        
        for i in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev, temp
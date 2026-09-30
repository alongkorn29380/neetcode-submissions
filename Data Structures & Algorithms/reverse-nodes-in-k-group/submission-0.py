# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            groupNext = kth.next
            prve, curr = groupNext, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prve
                prve = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = prve
            groupPrev = tmp
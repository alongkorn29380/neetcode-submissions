# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prve = None
        cur = head

        while cur:
            temp = cur.next # 0, 1, 2, 3
            cur.next = prve # None, 0, 1, 2 ,3
            prve = cur # 
            cur = temp
        return prve

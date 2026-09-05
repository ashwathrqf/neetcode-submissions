# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        if p==None:
            return p
        if p.next==None:
            return p
        q=p.next
        p.next=None
        c=p
        p=q
        q=q.next
        p.next=c

        while q!=None:
            c=p
            p=q
            q=q.next
            p.next=c
        return p



        
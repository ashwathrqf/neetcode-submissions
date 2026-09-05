# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=list1
        q=list2
        if not p:
            return list2
        if not q:
            return list1
        if p.val<q.val:
            a=list1
            p=p.next
        else:
            a=list2
            q=q.next
        head=a    
        while p and q:
            if p.val<q.val:
                a.next=p
                p=p.next
            else:
                a.next=q
                q=q.next
            a=a.next
        a.next=p if p else q
        return head








        
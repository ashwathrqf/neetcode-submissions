# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p=head
        q=p.next if p else None
        while p and q:
            if p==q:
                return True
            p=p.next
            q=q.next.next if q.next else None
        return False
            
        
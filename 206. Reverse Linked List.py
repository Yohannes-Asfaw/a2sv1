# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse=None
        while head:
            
            next1=head.next
            head.next=reverse
            reverse=head
            head=next1
        return reverse
            
            
            

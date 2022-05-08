# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        next1=head.next
        while curr.next:
            while next1:
                if curr.val >next1.val:
                    curr.val,next1.val=next1.val,curr.val
                next1=next1.next
            curr=curr.next
            next1 = curr.next
        return head
                
        

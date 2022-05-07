# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = merged = ListNode(None)
        while l1 and l2:
            
            if l1.val < l2.val:
                prev.next = l1 
                l1 = l1.next 
            else:
                prev.next = l2 
                l2 = l2.next 
            prev = prev.next 
        prev.next = l1 or l2 
        return merged.next

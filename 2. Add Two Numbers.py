# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur=out=ListNode()
        carry=0
        while l1 and l2:
            val = (l1.val+l2.val+carry)%10
            cur.val = val
            carry = (l1.val+l2.val+carry)//10
            l1=l1.next
            l2=l2.next
            if l1 or l2:
                cur.next=ListNode()
                cur=cur.next
        while l1:
            val = (l1.val+carry)%10
            cur.val = val
            carry = (l1.val+carry)//10
            l1=l1.next
            if l1:
                cur.next=ListNode()
                cur=cur.next
        while l2:
            val = (l2.val+carry)%10
            cur.val = val
            carry = (l2.val+carry)//10
            l2=l2.next
            if l2:
                cur.next=ListNode()
                cur=cur.next
        if carry:
            cur.next=ListNode(carry)
        return out

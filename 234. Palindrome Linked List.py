    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        even = False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next:
            even = True
            
        mid = slow
        after = slow.next
        while after:
            prev = mid
            mid = after
            after = after.next
            mid.next = prev
        
        while head != slow:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        
        if even: 
            if head.val != mid.val:
                return False
        
        return True

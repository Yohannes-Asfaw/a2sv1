    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        removed =  ListNode(0)
        removed.next=head
        check=removed
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head=head.next
                check.next=head.next
                
            else:
                check=check.next
            
            head=head.next
        print(check)
        return removed.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        temp = head
        while temp != None:
            a.append(temp.val)
            temp = temp.next
        for i in range(0,len(a),2):
            if i == len(a)-1:
                break
            a[i],a[i+1] = a[i+1],a[i]
        temp = head
        for i in range(len(a)):
            temp.val = a[i]
            temp = temp.next
        return head

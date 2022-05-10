    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr=head
        arr=[]
        ans=[]
        stack=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        ans.append(0)
        stack.append(arr[-1])
        for i in range(len(arr)-2,-1,-1):
            while(stack and stack[-1]<=arr[i]):
                stack.pop()
            if(not stack):
                ans.append(0)
            else:
                ans.append(stack[-1])
            stack.append(arr[i])
        return ans[::-1]

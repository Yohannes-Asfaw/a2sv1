  def kthLargestNumber(self, nums: List[str], k: int) -> str:
        list1=[]
        for i in nums:
            j=int(i)
            list1.append(j)
        list1.sort()
        list1.reverse()
        return str(list1[k-1])

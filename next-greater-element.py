class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check=[]
        ans=[]
        for i in nums1:
            if i in nums2:
                if i==nums2[-1]:
                    ans.append(-1)
                    continue
                if i in check:
                    check.remove(i)
                check.append(i)
                n=nums2[nums2.index(i)+1:]
                for j in n:
                    if j>i:
                        ans.append(j)
                        break
                    elif j==nums2[-1]:
                        ans.append(-1)
        return ans
                    
                

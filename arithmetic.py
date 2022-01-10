    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
            boollist = []
            for i in range(len(l)):
                x = 1
                newlist = nums[l[i]:r[i] + 1]
                newlist.sort()
                diff=newlist[1] - newlist[0]
                for i in range(2, len(newlist)):
                    if newlist[i] - newlist[i - 1] != diff:
                        boollist.append(False)
                        x=0
                        break
                    else:
                        x=1
                if x == 1:
                    boollist.append(True)
            return boollist

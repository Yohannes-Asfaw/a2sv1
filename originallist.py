    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dict = Counter(changed)
        changed.sort()
        changed1 = list(dict.keys())
        nums1 = []
        x=0
        if len(changed) % 2 != 0:
            return []
        else:
            for i in changed:
                if i == 0 and len(changed1) == 1:
                    for j in range(dict[i] // 2):
                        nums1.append(i)
                    return nums1
                elif i == 0 and len(changed1) != 1 and x==0:
                    for j in range(dict[i] // 2):
                        nums1.append(i)
                    x=1
                else:
                    if i * 2 in dict and i!=0:
                        if dict[i * 2] >0 and dict[i] > 0:
                                nums1.append(i)
                                dict[i]-=1
                                dict[i*2]-=1
            print(nums1)
            if len(changed) // 2 == len(nums1):
                return nums1
            else:
                return []

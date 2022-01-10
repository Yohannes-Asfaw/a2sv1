    def minSetSize(self, arr: List[int]) -> int:
        dict = {}
        for i in arr:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        count = 0
        i=0
        m=len(arr)
        while m > len(arr) // 2:
            m -= dict[i][1]
            count += 1
            i+=1

        return count

 def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list2 = []
        list3 = set(nums)
        list4 = list(list3)
        list5 = []
        nums.sort()
        for i in list4:
            list2.append(nums.count(i))
        for i in range(k):
            list5.append((list4[list2.index(max(list2))]))
            list2[list2.index(max(list2))] = 0
        return list5

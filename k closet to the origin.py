import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        list2 = []
        dict = []
        for i in points:
            d = (pow(i[0], 2) + pow(i[1], 2))
            dict.append([i,d])

        list1 = sorted(dict, key=lambda x: x[1])
        for i in range(k):
            list2.append((list1[i][0]))
        return list2

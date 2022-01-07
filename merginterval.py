class Solution:
    def merge(self, list1: List[List[int]]) -> List[List[int]]:
        list1 = sorted(list1)
        list2 = [list1[0]]
        list3 = [list1[0]]
        if len(list1) == 1:
            return list1
        for i in range(1, len(list1)):
            if list2[0][0] <= list1[i][0] <= list2[0][1] <= list1[i][1]:
                list3[-1]=([list2[0][0], list1[i][1]])
                list2[0]=list3[-1]
            elif list2[0][0] <= list1[i][0] <= list2[0][1] >= list1[i][1]:
                list3[-1]=(list2[-1])
                list2[0]=list3[-1]
            else:
                list3.append(list1[i])
                list2[0] = list3[-1]

        return list3

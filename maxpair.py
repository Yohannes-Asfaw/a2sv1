from typing import List
import math

class Solution:
    def maxOperations(self, nums, k):
        count = 0
        noofpairs = {}
        for i in nums:
            if i in noofpairs:
                noofpairs[i] = noofpairs[i] + 1
            else:
                noofpairs[i] = 1

        for n in noofpairs:
            sub = k - n
            if sub in noofpairs and noofpairs[sub] > 0:
                j = 0
                if n == k // 2:
                    j = math.floor(noofpairs[n] // 2)
                else:
                    j = min(noofpairs[n], noofpairs[sub])

                count += j
                noofpairs[sub] = noofpairs[sub] - j
                noofpairs[n] = noofpairs[n] - j

        return count

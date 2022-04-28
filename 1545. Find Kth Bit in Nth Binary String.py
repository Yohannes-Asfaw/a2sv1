class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            tempostr=""
            for i in str(s):
                if i=="0":
                    tempostr+="1"
                elif i=="1":
                    tempostr+="0"
            return tempostr[::-1]
            
        def bit(n):
            if n==1:
                return "0"
            else:
                return bit(n-1) + "1"+ reverse(bit(n-1))
        return bit(n)[k-1]

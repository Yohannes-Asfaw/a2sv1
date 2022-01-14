    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num)
        if length == k:
            return "0"
        
        num1 = []
        
        for i, j in enumerate(num):
            while num1 and int(num1[-1]) > int(j) and k:
                num1.pop()
                k -= 1
                
            num1.append(j)
        
        while k:
            num1.pop()
            k -= 1
                
        return str(int("".join(num1)))

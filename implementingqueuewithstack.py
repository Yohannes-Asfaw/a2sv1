    def __init__(self):
        self.minstack=[]
        self.minstack1=[]
        

    def push(self, x: int) -> None:
        self.minstack.append(x)
        
        

    def pop(self) -> int:
        while len(self.minstack)>0:
            self.minstack1.append(self.minstack.pop())
            
        x=self.minstack1.pop()
        while len(self.minstack1)>0:
            self.minstack.append(self.minstack1.pop())

        
        return x
        
        

    def peek(self) -> int:
         return self.minstack[0]
        

    def empty(self) -> bool:
        if len(self.minstack)==0:
            return True
        else:
            return False

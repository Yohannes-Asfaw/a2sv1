  class min_stack: 
  
  def __init__(self):
        self.lst = []
        
    def push(self, val: int) -> None:
        self.lst.append(val)
        self.minval = self.lst[0]
        for i in self.lst:
            if i < self.minval:
                self.minval = i
    def pop(self) -> None:
        self.lst.pop()
        if len(self.lst)>0:
            self.minval = self.lst[0]
            for i in self.lst:
                if i < self.minval:
                    self.minval = i
    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.minval

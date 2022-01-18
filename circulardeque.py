class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [] 
        self.k = k 
        

    def insertFront(self, value: int) -> bool:
        if len(self.deque) <self.k:
            self.deque = [value] + self.deque 
            return True 
        else:
            return False 
        
    def insertLast(self, value: int) -> bool:
        if len(self.deque) <self.k:
            self.deque =  self.deque +[value]
            return True 
        else:
            return False   

    def deleteFront(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop(0) 
            return True 
        else:
            return False 

    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop() 
            return True 
        else:
            return False 

    def getFront(self) -> int:
        if len(self.deque) > 0 : 
            return self.deque[0]
        else:
            return -1 

    def getRear(self) -> int:
        if len(self.deque) > 0 : 
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0 

    def isFull(self) -> bool:
        return len(self.deque) == self.k

class RecentCounter:


    def __init__(self):
        self.calls = []
 
    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.pop(0)
        return len(self.calls)

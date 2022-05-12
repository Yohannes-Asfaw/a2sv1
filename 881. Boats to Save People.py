    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res=0
        front=0
        back=len(people) - 1
        while front<=back:
            res+=1
            if people[front] + people[back]<=limit:
                front+=1
            back-=1
        return res
        

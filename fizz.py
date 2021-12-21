  def fizzBuzz(self, n: int) -> List[str]:
        x=[]
        for i in range(n):
            if (i+1)%3==0 and (i+1)%5!=0:
                x.append("Fizz")
            elif (i+1) % 3 != 0 and (i+1) % 5 == 0:
                x.append("Buzz")
            elif (i+1) % 3 != 0 and (i+1) % 5 != 0:
                x.append(f'{(i+1)}')
            elif (i+1) % 3 ==0 and (i+1) % 5 == 0:
                x.append("FizzBuzz")
        return x

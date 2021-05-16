class CountValueFor:

    def __init__(self,value: int = 0,increment: int = 1) -> None:
        self.val = value
        self.incr = increment
    
    def __repr__(self) -> str:
        return str(self.val)
    
    def increase(self) -> None:
        self.val += self.incr

a = CountValueFor()
b = CountValueFor(10,100)
c = CountValueFor(increment = 25)
a.increase()
b.increase()
c.increase()
print(a.val, b.val, c.val)
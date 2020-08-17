class Calci:
    def add(a,b):
        return a + b
    def mul(a,b):
        return a * b
class Modu:
    def power(aval,bval):
        return aval ** bval
    def isEven(val):
        if val % 2 == 0:
            return True
        return False
class Calci1:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
    def __add__(self):
        return self.val1 + self.val2
    def __mul__(self):
        return self.val1 * self.val2
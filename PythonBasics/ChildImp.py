from OOPSDemo import Calcualtor


class ChildImp(Calcualtor):

    num2=200

    def __init__(self,a,b):
        Calcualtor.__init__(self,a,b)

    def getcompletedata(self):

        return self.num2 + self.num1 + self.summation()


obj2= ChildImp(5,6)
print(obj2.getcompletedata())
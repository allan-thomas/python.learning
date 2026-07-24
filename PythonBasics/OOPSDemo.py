class Calcualtor:

    num1=100

    def __init__(self,a,b):
        print("Constructor is called")
        self.firstnum=a
        self.secondnum=b

    def getdata(self):
        print("Calculator class has been created")

    def summation(self):
        return self.firstnum + self.secondnum + Calcualtor.num1

obj = Calcualtor(1,2)
obj.getdata()
print(obj.num1)
print(obj.summation())

obj1= Calcualtor(3,4)
print(obj1.summation())
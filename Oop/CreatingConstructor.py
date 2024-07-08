class Operation1:
    def __init__(self):
        print('constructor 1 Called')
        
        self.a = 10
        self.b = 20
         
    def add(self):
        print(self.a + self.b)


o1 = Operation1()

o1.add()





class Operation2:
    def __init__(self,a,b):
        print('constructor 2 Called')
        
        self.a = a
        self.b = b
         
    def add(self):
        print(self.a + self.b)


o2 = Operation2(10,20)

o2.add()


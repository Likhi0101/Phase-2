class graph:
    def __init__(self):
        self.d={}
    def addegde(self,a,b):
        if a not in self.d:
            self.d[a]=[]
            self.d[a].append(b)
        else:
            self.d[a].append(b)
    def printList(self):
        print(self.d)
t=graph()
t.addegde(1,2)
t.addegde(1,4)
t.addegde(2,1)
t.addegde(2,3)
t.addegde(3,2)
t.addegde(3,4)
t.addegde(4,1)
t.addegde(4,3)
t.printList()


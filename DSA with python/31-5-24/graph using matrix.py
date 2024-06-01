class graph:
    def __init__(self):
        self.g=[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]
    def addegde(self,a,b):
        for i in range(0,len(self.g)-1):
            for j in range(0,len(self.g[0])-1):
                if i+1==a and j+1==b:
                    self.g[a][b]=1
    def printList(self):
        for i in self.g:
            for j in i:
                print(j,end="")
            print()
t=graph()
print(t.g)
t.addegde(1,2)
t.addegde(1,4)
t.addegde(2,1)
t.addegde(2,3)
t.addegde(3,2)
t.addegde(3,4)
t.addegde(4,1)
t.addegde(4,3)
t.printList()


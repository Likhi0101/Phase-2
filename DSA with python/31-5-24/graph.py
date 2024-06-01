class graph:
    def __init__(self):
        self.g=[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]
    def addedge(self,a,b):
        for i in range(0,len(self.g)-1):
            for j in range(0,len(self.g[0])-1):
                if i+==a and j+1==b:
                    self.g[a][b]=1
    def printList(self):
        for i in self.g:
            for j in i:
                print(j,end="")
            print()
t=graph()
t.addedge(1,2)
t.addedge(1,2)
t.addedge(1,2)
t.addedge(1,2)
t.addedge(1,2)
t.addedge(1,2)
t.addedge(1,2)
t.addedge(1,2)
t.addedge(1,2)

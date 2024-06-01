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
       
    def bfs(self,root):
        queue=[root]
        visited=[root]
        while queue:
            curr=queue.pop(0)
            print(curr)
            if curr in self.d:
                for i in self.d[curr]:
                    if i not in visited:
                        visited.append(i)
                        queue.append(i)
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
t.bfs(1)

                        
                    
            

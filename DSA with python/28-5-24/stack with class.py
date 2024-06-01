class stack:
    def __init__(self):
        self.l=[]
    def push(self,data):
        self.l.append(data)
    def pop(self):
        self.l.pop()  
    def peek(self):
        print(self.l[-1])
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
print(s.l)
s.peek()

'''pop(0) becomes queue'''

class node:
    def __init__(self,data=0):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insertatbeg(self,value):
        newnode = node(value)
        if self.head==None:
            self.head=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
    def insertatend(self,value):
        newnode=node(value)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def delatbeg(self):
        if not self.head:
            return
        else:
            self.head=self.head.next
    def delatend(self):
        if not self.head:
            return
        if self.head.next==None:
            self.head==None
        else:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None
    def count(self,value):
        c=1
        curr=self.head
        while curr.next:
            c+=1
            curr=curr.next
        print(c)
        m=c//2
        #print(m)
        i=1
        curr=self.head
        while i!=m+1:
            curr=curr.next
            i+=1
            newnode=node(value)
            newnode.next=curr.next
            curr.next=newnode
        #print(curr.data)
    def search(self,value,data):
        curr=self.head
        newnode=node(data)
        while curr:
            if curr.data==value:
                print("yes")
                newnode=curr.next
                curr=newnode
                break
            curr=curr.next
        else:
            print("no")
    
a=linkedlist()
a.insertatbeg(1)
a.insertatbeg(2)
a.insertatbeg(3)
a.insertatbeg(4)
a.insertatbeg(5)
'''a.delatbeg()
a.delatend()'''
a.printlist()
a.count(value3 data7)
'''a.search(2)'''

        

l=[0,1,2,3,5,6,7,8]
def partition(l,beg,end):
    pi=l[beg]
    start=beg+1
    stop=end
    while True:
        while start<len(l) and l[start]<pi:
            start+=1
        while stop>-1 and l[stop]>pi:
            stop-=1
        if start<stop:
            l[start],l[stop]=l[stop],l[start]
        else:
            break
    l[beg],l[stop]=l[stop],l[beg]
    return stop
def quick(l,i,j):
    if i<j:
        p=partition(l,i,j)
        quick(l,i,p-1)
        quick(l,p+1,j)
quick(l,0,len(l)-1)
print(l)

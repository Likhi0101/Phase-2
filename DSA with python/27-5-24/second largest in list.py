l=[1,2,3,9,6,4,8]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
s=l[0]
for i in range(len(l)):
    if l[i]>s and l[i]!=m:
        s=l[i]
print(s)

'''
l=[0,8,7,4,6]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
s=min(l)
for i in range(len(l)):
    if l[i]!=m and l[i]>s:
        s=l[i]
print(s)
'''

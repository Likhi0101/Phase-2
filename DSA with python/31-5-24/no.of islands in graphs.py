#1=land,0=water
map=[[1,1,0,0,1],[1,1,0,0,1],[0,0,1,0,0],[1,0,1,0,1],[1,0,1,0,1]]
c=0
def helper(map,i,j):
    if i==5 or j==5:
        return
    if map[i][j]==0:
        return
    if i<0 or j<0:
        return
    map[i][j]=0
    helper(map,i-1,j)
    helper(map,i+1,j)
    helper(map,i,j+1)
    helper(map,i,j-1)
    return
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]==1:
            c+=1
            map[i][j]==0
            helper(map,i,j)
print(c)

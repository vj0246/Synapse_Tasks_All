matrix=[[1,0,0,0,1],[1,0,1,1,1],[1,1,0,1,1],[1,0,1,1,0],[0,1,0,1,1]] 

m=int(input("Please enter size of region affected from bombing:"))

max_count=0

def matrix_maker(x,y):
    lst=list()
    for i in range(max(0,y-1),min(y-1+m,4)):#min(y-1+m,5)?
        for j in range(max(0,x-1),min(x-1+m,4)):
            lst.append(matrix[i][j])
    return lst

def destroyer_calculator(lst):
    count=0
    for i in lst:
        if i==1:
            count+=1
    return count

for i in range(0,5):
    for j in range(0,5):
        if matrix[i][j]==1:
            temp=(destroyer_calculator(matrix_maker(j,i)))
            if temp>max_count:
                max_count=temp

print(max_count)








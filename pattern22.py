l=[4,3,2]
j=0
for i in range(1,4):
    h=l[j]
    print(" "*h,end='')
    print(' *'*i)
    j=j+1
print(' * * * * * ')
l=l[::-1]
j=0
i=3
while(i!=0):
    h=l[j]
    print(" "*h,end='')
    print(' *'*i)
    j=j+1
    i=i-1

l=[1,2,3,4]
k=[7,5,3,1]
j=0
for i in k:
    h=l[j]
    print('  '*h,end='')
    print(" *"*i,end='')
    j=j+1
    print("\n")
l=l[::-1]
k=k[::-1]
j=0
for i in k:
    h=l[j]
    print('  '*h,end='')
    print(" *"*i,end='')
    j=j+1
    print("\n")

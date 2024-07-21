l=[5,4,3,2,1]
h=4
for i in range(1,6):
    for j in l:
        print(j,end=' ')
    k=l[::-1]
    for x in k:
        print(x,end=' ')
    l.remove(l[h])
    h=h-1
    print('\n')

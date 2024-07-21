l=[9,7,5,3,1]
for i in range(0,len(l)):
    if i==0:
        print('*'*l[i])
    else:
        k=i
        while(k!=0):
            print(' ',end='')
            k=k-1
        print('*'*l[i])
    
    

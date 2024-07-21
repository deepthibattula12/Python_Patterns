l=[6,5,4,3,2,1,0] #spaces
for i in range(0,7):
    if i!=6:
        k=l[i]
        print(' '*k,end='')
        for j in range(0,i+1):
            print(' *',end='')
        print('\n')
    else:
        print('*'*l[i])
        

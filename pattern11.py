j=[1,3,5,7,9]
h=0
for i in range(1,6):
    v=0
    while(v!=i):
        print(str(i)*j[h])
        v=v+1
        h=h+1
    print('\n')

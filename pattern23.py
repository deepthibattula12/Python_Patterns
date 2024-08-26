n=4
for i in range(n+1):
  if i==1:
    print("4"*4)
  elif i==2 or i==3:
    print("4","3"*2,"4",sep='')
  elif i==4:
    print("4"*4)
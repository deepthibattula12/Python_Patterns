n=6
for i in range(n+1):
  if i==1 or i==6:
    print("6"*6)
  elif i==2 or i==5:
    print("6","5"*4,"6",sep='')
  elif i==3 or i==4:
    print("6","5","4"*2,"5","6",sep='')
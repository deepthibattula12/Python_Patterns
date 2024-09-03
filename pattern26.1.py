n=7
for i in range(n+1):
    if i%2!=0:
        p=".|."*i #This pattern should be in the middle
        print(p.center(27,'-'))#so for that we have used center method
print("WELCOME".center(27,'-'))
while(n!=0):
    if n%2!=0:
        p=".|."*n
        print(p.center(27,'-'))
    n=n-1

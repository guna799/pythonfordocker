n=int(input("enter n value"))
s=0
for i in range(0,n):
    if(i%2!=0):
        print("i value is :",i)
        s=s+i
print("sum of all odd numbers is :",s)

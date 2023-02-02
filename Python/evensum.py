n=int(input("enter n value"))
s=0
for i in range(0,n):
    if(i%2==0):
        s=s+i
        print("i vlaue is :", i)        
print("sum of all even numbers are :",s)

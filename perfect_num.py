user=int(input("enter any number"))
sum=0
i=1
while i<user:
    if user%i==0:
        per=i
        sum=sum+per
if sum==user:
    print("perfect number")
else:
    print("not perfect number")
i=i+1
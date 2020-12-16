user=int(input("enter the number"))
i=2
while i<=user:
    if user%i==0:
        print("not prime")
        break
    i=i+1
else:
    print("prime")
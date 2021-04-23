user=int(input("enter the number"))
count=0
i=1
while i<user:
    if user%i==0:
        count=count+1
        
    i=i+1
if count==1:
    print(user,"prime")
else:
    print(user,"not prime")

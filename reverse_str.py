def string (name):
    i= len(name)
    r=""
    while i>0:
        r.append(name[i-1])
        i=i-1
    print(r)
user=int(input("enter any number"))
string(user)
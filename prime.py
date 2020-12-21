n = 2
count = 0
while(count < 5):
    isPrime = True
    i = 2
    while(i<n):
        if n%i == 0:
            isPrime = False
        i = i + 1
    if (isPrime):
        print (str(n) + "is prime")
        count += 1
    n = n + 1  
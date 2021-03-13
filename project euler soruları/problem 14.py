def collatz (x):
    while x>1:
        if x%2==0:
            x = x / 2
            print(x)

        elif x%2==1:
            x = 3 * x + 1
            print (x)
        if x==1:
            break

print (collatz (999999))
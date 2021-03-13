for i in range (1,1001):
    for j in range (1,1001):
        a=i*j
        if (a//100000 == a%10 and (a//10000)%10== (a%100)//10 and (a//1000)%10 == (a//100)%10 ):
            print (a)
a=1
b=2
fibonacci=[a,b]
while (a+b<4000000):
    a,b=b,a+b
    fibonacci.append(b)
print (fibonacci)


toplam=1
for i in fibonacci:
    if i%2==1:
        toplam=toplam+i
print (toplam)
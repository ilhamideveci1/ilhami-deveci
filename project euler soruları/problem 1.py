toplam=0
i=1
while i<1000:
    if i%3==0 or i%5==0:
        toplam=toplam+i
    i=i+1

print (toplam)
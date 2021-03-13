def asal_mi(sayı):
    for i in range(2, sayı):
        if (sayı % i == 0):
            return False
    return sayı
toplam=0
for i in range(2,2000001):
    if asal_mi(i):
        toplam+=i

print(toplam)
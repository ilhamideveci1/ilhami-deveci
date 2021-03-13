def asal_mi(sayı):



        for i in range(2,sayı):
            if (sayı % i == 0):
                return False
        return sayı
sonuc=list()
for i in range (2,180300):
    if type(asal_mi(i))== int:
        sonuc.append(i)
print (sonuc)
print (len(sonuc))
print (sonuc[10000])
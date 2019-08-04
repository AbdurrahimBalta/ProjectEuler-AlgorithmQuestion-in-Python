#he prime factors of 13195 are 5, 7, 13 and 29.
#What is t#13195 sayısının asal bölenleri 5-7-13-29 dur buna göre aşşağıdaki sayının en büyük asal böleni nedir

def asal(Sayi):
    AsalBolen = 2
    Dizi = list()
    while Sayi >= AsalBolen:
        if Sayi % AsalBolen == 0:
            Sayi = Sayi / AsalBolen
            Dizi.insert(len(Dizi),AsalBolen)
        else:
            AsalBolen += 1
    return Dizi
print(asal(600851475143))

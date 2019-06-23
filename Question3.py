#he prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#13195 sayısının asal bölenleri 5-7-13-29 dur buna göre aşşağıdaki sayının en büyük asal böleni nedir

Sayi : int = 600851475143
AsalBolen : int = 2
Dizi = list()
#Sayinin tüm asal bölenleri bulunur
while Sayi >= AsalBolen:
    if Sayi % AsalBolen == 0:
        Sayi = Sayi / AsalBolen
        Dizi.insert(len(Dizi), AsalBolen)
    else:
        AsalBolen += 1
print(Dizi)
print(Dizi[len(Dizi)-1])


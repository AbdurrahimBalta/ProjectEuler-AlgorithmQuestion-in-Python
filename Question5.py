# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""1’den 20’ye kadar olan sayılara eşit olarak bölünebilen en küçük pozitif sayıyı bulan algoritma"""
def obeb(sayi1,sayi2):

    for i in range(int((sayi1+sayi2)/2),0,-1):      #Başlangıç değerinin s1+s2 olmasının nedeni iki sayının toplamının yarısı her türlü küçük olan sayıya
         if sayi1 % i == 0 and sayi2 % i == 0:      #Büyük eşit durumunda olacaktır ve döngüyü kısaltmak amaçlanmıştır
            break
    return i

def okek(sayi1,sayi2):

    okek = (sayi1*sayi2) / obeb(sayi1,sayi2) # Okek = sayılar çarpımı bölü obeb
    print(okek)
    return okek

GenelEkok : int = 0
a : int = 1
b : int = 2
while b <= 20:
    a = okek(a,b)
    b += 1
print(a)



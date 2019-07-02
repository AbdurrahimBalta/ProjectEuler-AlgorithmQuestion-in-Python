# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""1’den 20’ye kadar olan sayılara eşit olarak bölünebilen en küçük pozitif sayıyı bulan algoritma"""
"""
IlkSayi: int = 5
DegisenSayi: int = 4
EnKucukAsalSayi: int = 2
EnKucukAsalSayi2: int = 2

while DegisenSayi != 1:
    if IlkSayi % EnKucukAsalSayi == 0:
        IlkSayi /= EnKucukAsalSayi
    else:
        EnKucukAsalSayi += 1
    if DegisenSayi % EnKucukAsalSayi2 == 0:
        DegisenSayi /= EnKucukAsalSayi2
    else:
        EnKucukAsalSayi += 1
    if EnKucukAsalSayi == IlkSayi:
        IlkSayi = IlkSayi * DegisenSayi
        DegisenSayi -= 1
        EnKucukAsalSayi = 2
        EnKucukAsalSayi2 = 2

print(IlkSayi)

"""
#Çözemedim hacılar daha
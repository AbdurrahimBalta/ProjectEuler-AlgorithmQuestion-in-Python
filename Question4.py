# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.20
# Find the largest palindrome made from the product of two 3-digit numbers.
IlkSayi: int = 100
SonSayi: int = 999
PalDizi = list()
#3 haneli en büyük palindroimk sayıyı bulan algoritma
while SonSayi >= IlkSayi:
    PalindromSayi: str = str(SonSayi * IlkSayi)

    if int(PalindromSayi) == int(PalindromSayi[::-1]):
        PalDizi.append(int(PalindromSayi))
        IlkSayi += 1
    elif int(PalindromSayi[::-1]) != int(PalindromSayi):
        IlkSayi += 1
    if SonSayi == IlkSayi:
        IlkSayi = 100
        SonSayi -= 1
PalDizi.sort()
print(PalDizi[len(PalDizi) - 1])

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
ToplamAsalSayi: int = 0
for i in range(3,2000000):
    bolundu = False
    for j in range(2,i):
            if i % j == 0:
                bolundu=True
    if bolundu == False:
        ToplamAsalSayi += i
        print(ToplamAsalSayi)
print(ToplamAsalSayi)
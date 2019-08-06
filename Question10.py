"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
def drange(basla, dur, atla):
    r = basla
    while r < dur:
        yield r
        r += atla
ToplamAsalSayi = list()
for i in range(3,2000000,2):
    bolundu = False
    uretec = drange(3,(i/2)+1,2)
    for j in uretec:

            if i % j == 0:
                bolundu=True

    if bolundu == False:
        print(i)
        ToplamAsalSayi.append(i)
        print(ToplamAsalSayi)
#Eğer soruyu yanlış anlayıp ilk 2 milyon asal sayının toplamını merak ederseniz aşşağıdaki.
#Algoritmayı anlamak için önce Erostosthenes kalburu sonrasında wheel factorization aramalarıyla
#Bir fikriniz olabilir. Şahsen ben yinede anlamadım:)
"""

def Z30_Sieve():
    spot = Z30_sieve_sv[0]
    pc = Z30_sieve_sv[spot] + 30
    Z30_sieve_sv[spot] = pc
    spot = spot + 1
    if spot < len(Z30_sieve_sv):
        Z30_sieve_sv[0] = spot
    else:
        Z30_sieve_sv[0] = 1
    return pc

Z30_sieve_sv = [2, 1, -23, -19, -17, -13, -11, -7, -1]
toplamasal: int = 0
for i in range(0, 260000):
    print( Z30_Sieve() , Z30_sieve_sv)
    toplamasal += Z30_Sieve()

print(toplamasal)"""


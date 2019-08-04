from math import sqrt
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
# İlk altı asal sayıyı listeleyerek: 2, 3, 5, 7, 11 ve 13, 6. asalın 13 olduğunu görebiliriz.
# 10001. asal sayı nedir ??

def drange(basla, dur, atla):
    r = basla
    while r < dur:
        yield r
        r += atla

AsalDizi = list()
i : int = 3
while len(AsalDizi) != 10000:
    bolundu = False
    uretec = drange(3, (i / 2) + 1, 2)

    for j in uretec:
            if i % j == 0:
                bolundu = True
                break
    if bolundu == False:
        print(i)
        AsalDizi.append(i)
    i += 2

print(AsalDizi[len(AsalDizi) - 1])



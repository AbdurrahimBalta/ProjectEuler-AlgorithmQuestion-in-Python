"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

a: int = 8
b: int = 15
c: int = 17
carpim: int = 0
while True:
    if a + b + c == 1000 and pow(a,2) + pow(b,2) == pow(c,2):
        carpim = a*b*c
        break
    else:
        a += 8
        b += 15
        c += 17
print(a)
print(carpim)

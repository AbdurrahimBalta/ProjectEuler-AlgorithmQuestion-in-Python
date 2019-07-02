"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

# İlk altı asal sayıyı listeleyerek: 2, 3, 5, 7, 11 ve 13, 6. asalın 13 olduğunu görebiliriz.
# 10001. asal sayı nedir ?


AsalDizi = list()

i : int = 3
while True:
    bolundu = False
    for j in range(2,i):
            if i % j == 0:
                bolundu = True
    if bolundu == False:
        print(i)
        AsalDizi.append(i)
    i+=1
    if len(AsalDizi) == 10002:
        break
print(AsalDizi[len(AsalDizi) - 1])

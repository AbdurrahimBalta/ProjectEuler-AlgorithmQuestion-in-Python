#Soru 2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
Ilk_Fibon_Deger: int = 1
Ortanca_Fibon_Deger: int = 1
Son_Fibon_Deger : int = 0
i : int = 0
# 4 milyondan küçük tüm çift fibon değerler
while (Ilk_Fibon_Deger <4000000 and Ortanca_Fibon_Deger < 4000000):

    Son_Fibon_Deger = Ilk_Fibon_Deger + Ortanca_Fibon_Deger
    Ortanca_Fibon_Deger = Son_Fibon_Deger
    Ilk_Fibon_Deger = Ortanca_Fibon_Deger + Ilk_Fibon_Deger

    if Ilk_Fibon_Deger % 2 == 0 and Ortanca_Fibon_Deger % 2 == 0:
        i += Ilk_Fibon_Deger
    elif Ilk_Fibon_Deger % 2 == 0:
        i += Ilk_Fibon_Deger
    elif Ortanca_Fibon_Deger % 2 == 0:
        i += Ortanca_Fibon_Deger

print(i)

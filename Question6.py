"""lk on doğal sayının karelerinin toplamı,

1 2 + 2 2 + ... + 10 2 = 385
İlk on doğal sayının toplamının karesi,

(1 + 2 + ... + 10) 2 = 55 2 = 3025
Dolayısıyla, ilk on doğal sayının karelerinin toplamı ile toplamın karesi arasındaki fark 3025 - 385 = 2640'dır.

İlk yüz doğal sayının karelerinin toplamı ile toplamın karesi arasındaki farkı bulun."""

a = int(input("Toplam karesinden kare toplamını çıkaracağınız sayıyı girin"))

Kare_Toplam : int = 0
Toplam_Kare : int = 0
Sonuc : int = 0

for i in range(1,a+1,1):
    Kare_Toplam += i*i

for i in range(1,a+1,1):
    Toplam_Kare += i

Toplam_Kare *= Toplam_Kare
Sonuc = Toplam_Kare - Kare_Toplam
print(Sonuc)

















# contoh program menghitung sisi miring dari segitiga siku-siku

# import library
import math # supaya kita bisa menghitung akar kuadrat

# input sisi
sisiA = float(input("masukkan sisi A: "))
sisiB = float(input("masukkan sisi B: "))

# hitung kuadrat dari masing-masing sisi
aKuadrat = sisiA ** 2
bKuadrat = sisiB ** 2

# hitung sisi miring
tmp_sisi_miring = aKuadrat + bKuadrat
sisi_miring = math.sqrt(tmp_sisi_miring)

# tampilkan hasil
print("sisi miring(C) : {}".format(sisi_miring))

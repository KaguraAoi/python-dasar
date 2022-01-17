print("======================================")
print("PROGRAM MENGHITUNG HARGA DENGAN DISKON")
print("======================================")

harga_belanja = input("masukan harga belanja anda : ")
harga_belanjaa = int(harga_belanja)

if harga_belanjaa >= 500000 :
  diskon = harga_belanjaa * 0.5
  total = harga_belanjaa - diskon
  print("harga belanja anda menjadi ", total)
elif harga_belanjaa >= 300000 :
  diskon = harga_belanjaa * 0.3
  total = harga_belanjaa - diskon
  print("harga belanja anda menjadi ", total)
elif harga_belanjaa >= 50000 :
  diskon = harga_belanjaa * 0.1
  total = harga_belanjaa - diskon
  print("harga belanja anda menjadi ", total)
else :
  print("maaf, anda tidak mendapatkan diskon")

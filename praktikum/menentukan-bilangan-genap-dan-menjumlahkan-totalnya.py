# contoh program menentukan bilangan genap dan menjumlahkan totalnya

tmp = 0

# input bilangan
for i in range (10) :
  bil = int(input("masukkan bilangan : "))
  tmp = tmp + bil # nilai yang sudah disimpan ke tmp akan dijumlahkan
  # dengan tmp yang baru
print("------------------------")
print("total : {}".format(tmp))

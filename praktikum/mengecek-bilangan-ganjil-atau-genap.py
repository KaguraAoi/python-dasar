# program menentukan bilangan suatu bilangan ganjil atau genap

# input bilangan
bilangan = int(input("masukkan angka : "))

# cek kondisi
if bilangan % 2 == 0 :
  print("{} adalah bilangan genap".format(bilangan))
elif bilangan % 2 == 1 :
  print("{} adalah bilangan ganjil".format(bilangan)) 

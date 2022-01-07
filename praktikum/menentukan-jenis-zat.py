# contoh program menentukan jenis zat

# input suhu
suhu = int(input("masukkan suhu dalam celcius: "))

# cek kondisi
if suhu < 0 :
  print("beku")
elif suhu > 100 :
  print("gas")
elif suhu >= 0 and suhu <= 100 :
  print("cair")

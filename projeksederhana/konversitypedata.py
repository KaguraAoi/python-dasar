# contoh 3 : program konversi tipe data

# --------
# function
# --------

# fungsi menu
def menuu() :
  print("1. string ke integer")
  print("2. string ke float")
  print("3. integer ke float")
  print("4. float ke integer")
  print("5. cek type data")
  print("----------------------------------")

def garis() :
  print("-------------------------------------")
    
# -------------
# program utama
# -------------

# menu
menuu()

# user input angka yang ingin dikonversi
angka = input("masukkan angka: ")

# user input pilihan
pilih = int(input("masukan pilihan(1/2/3/4/5): "))

garis()

# cek kondisi
if pilih == 1 :
  print(angka, type(angka))
  print("-- konversi --")
  konversi = int(angka)
  print(konversi, type(konversi))
  print("konversi sukses")
  print("----------------------")
elif pilih == 2 :
  print(angka, type(angka))
  print("-- konversi --")
  konversi = float(angka)
  print(konversi, type(konversi))
  print("konversi sukses")
  print("----------------------")
elif pilih == 3 :
  konversi1 = int(angka)
  print(konversi1, type(konversi1))
  print("-- konversi --")
  konversi2 = float(konversi1)
  print(konversi2, type(konversi2))
  print("konversi sukses")
  print("----------------------")
elif pilih == 4 :
  konversi1 = float(angka)
  print(konversi1, type(konversi1))
  print("-- konversi --")
  konversi2 = int(konversi1)
  print(konversi2, type(konversi2))
  print("konversi sukses")
  print("----------------------")
else :
  print("maaf, input yang anda masukkan tidak tersedia")

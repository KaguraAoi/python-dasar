# contoh 2 : contoh program kalkulator sederhana

# --------
# FUNCTION
# --------

# fungsi penjumlahan
def penjumlahan(x, y) :
  return x + y
    
# fungsi pengurangan
def pengurangan(x, y) :
  return x - y

# fungsi perkalian
def perkalian(x, y) :
  return x * y

# fungsi pembagian
def pembagian(x, y) :
  return x / y
    
# -------------
# PROGRAM UTAMA
# -------------

# input user angka
bil1 = float(input("masukkan angka pertama: "))
bil2 = float(input("masukkan angka kedua  : "))

# menu operator
print("1.penjumlahan(+)")
print("2.pengurangan(-)")
print("3.perkalian(x)")
print("4.pembagian(:)")

# pemilihan operator
pilih_operator = int(input("pilih operator dengan menginput angka(1/2/3/4): "))

# proses
if pilih_operator == 1 :
  print("{} + {} = {}".format(bil1, bil2, penjumlahan(bil1, bil2)))
elif pilih_operator == 2 :
  print("{} - {} = {}".format(bil1, bil2, pengurangan(bil1, bil2)))
elif pilih_operator == 3 :
  print("{} x {} = {}".format(bil1, bil2, perkalian(bil1, bil2)))
elif pilih_operator == 4 :
  print("{} : {} = {}".format(bil1, bil2, pembagian(bil1, bil2)))

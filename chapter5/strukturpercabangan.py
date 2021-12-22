# apa itu percabangan dan kenapa dinamakan percabangan?
# -----------------------------------------------------
# untuk menggambarkan alur program yang bercabang
# percabangan juga disebut control
# percabangan akan membuat program berpikir dan menentukan tindakan sesuai dengan logika/kondisi yang kita berikan

# struktur percabangan if
# -----------------------
# percabangan if digunakan saat terdapat satu pilihan keputusan
# bagian condition berperan sebagai penentu dari struktur percabangan 
# jika condition benar(True), blok kode program akan dijalankan. jika condition tidak benar(False), blok kode program tidak akan dijalankan
# blok kode program dalam bahasa Python ditandai dengan (:) setelah penulisan condition, kemudian diikuti satu atau beberapa baris dengan awalan indentasi

# contoh 1
# ------
a = 12
b = 5

if a > b :
  print("variabel a lebih besar dari variabel b") # variabel a lebih besar dari variabel b
  
# contoh 2
# --------
lulus = input("apakah kamu lulus? [ya/tidak]: ")

if (lulus == "tidak") :
  print("kamu harus ikut ujian") # jika tidak maka jawabannya "kamu harus ikut ujian"
    
# contoh 3
# --------
a = 9
    
if (a % 2 == 0) :
  print(a, "merupakan bilangan genap")
if (a % 2 != 0) :
  print(a, "merupakan bilangan ganjil") # 9 merupakan bilangan ganjil
    
# struktur percabangan if else
# percabangan if else digunakan saat terdapat dua pilihan keputusan
# pada dasarnya, kondisi if else merupakan modifikasi tambahan dari kondisi if
# saat if bernilai False maka bagian else yang akan dijalankan

# contoh 1
# --------
umur = int(input("berapa umur kamu: "))

if umur >= 18 :
  print("kamu boleh membuat SIM")
else :
  print("Kamu belum boleh membuat SIM")

# contoh 2
# --------
a = 10

if (a % 2 == 0) :
  print(a, "merupakan bilangan genap") # a merupakan bilangan genap
else :
  print(a, "merupakan bilangan ganjil") 
  
# contoh 3
# --------
a = int(input("masukkan nilai a : ")) # 5
b = int(input("masukkan nilai b : ")) # 7

if a < b : # True
  print("nilai terbesar adalah ", b) # 7
  print("nilai terkecil adalah ", a) # 5
else:
  print("nilai terbesar adalah ", a)
  print("nilai terkecil adalah ", b)

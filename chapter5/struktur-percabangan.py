# apa itu percabangan ?
# ---------------------
# percabangan digunakan untuk menggambarkan alur program yang bercabang
# percabangan akan menentukan tindakan sesuai dengan logika/kondisi yang kita berikan

# struktur percabangan if
# -----------------------
# percabangan if digunakan saat terdapat satu pilihan keputusan
# bagian condition berperan sebagai penentu dari struktur percabangan 
# jika condition benar(True), blok kode program akan dijalankan
# jika condition tidak benar(False), blok kode program tidak akan dijalankan
# blok kode program dalam bahasa python ditandai dengan (:) setelah penulisan condition, 
# kemudian diikuti satu atau beberapa baris dengan awalan indentasi

# contoh 1
# --------
a = 12
b = 5

if a > b :
  print("variabel a lebih besar dari variabel b") # True, maka blok program dijalankan
  
# contoh 2
# --------
lulus = input("apakah kamu lulus ? [ya/tidak] : ") # tidak

if (lulus == "tidak") :
  print("kamu harus ikut ujian") # jika True maka blok program dijalankan
    
# contoh 3
# --------
a = 9
    
if (a % 2 == 0) :
  print(a, " merupakan bilangan genap")
if (a % 2 != 0) :
  print(a, " merupakan bilangan ganjil") # True, 9 merupakan bilangan ganjil
    
# struktur percabangan if else
# ----------------------------
# percabangan else digunakan saat terdapat dua pilihan keputusan
# pada dasarnya, kondisi else merupakan modifikasi tambahan dari kondisi if
# saat if bernilai False maka bagian else yang akan dijalankan

# contoh 1
# --------
umur = int(input("berapa umur kamu : ")) # misal 20

if umur >= 18 :
  print("kamu boleh membuat SIM") # jika True maka blok program dijalankan
else : 
  print("Kamu belum boleh membuat SIM") # jika False maka jalankan ini

# contoh 2
# --------
a = 10

if (a % 2 == 0) :
  print(a, " merupakan bilangan genap") # True, 10 merupakan bilangan genap
else :
  print(a, " merupakan bilangan ganjil") 
  
# contoh 3
# --------
a = int(input("masukkan nilai a : ")) # misal 5
b = int(input("masukkan nilai b : ")) # misal 7

if a < b : # True
  print("nilai terbesar adalah ", b) # 7
  print("nilai terkecil adalah ", a) # 5
else:
  print("nilai terbesar adalah ", a)
  print("nilai terkecil adalah ", b)

# struktur percabangan elif (else if)
# -----------------------------------
# percabangan elif digunakan apabila terdapat lebih dari dua kondisi
# jika kondisi if bernilai False, maka program akan lanjut ke kondisi elif
# jika elif juga tidak terpenuhi maka akan lanjut ke elif selanjutnya
# (tergantung jumlah elif yang diberikan) sehingga blok else terakhir bernilai True

# contoh 1
# --------
# nilai = 'D'

if nilai == 'A' :
  print("pertahankan terus")
elif nilai == 'B' :
  print("harus lebih baik lagi")
elif nilai == 'C' :
  print("perbanyak belajar lagi")
elif nilai == 'D' :
  print("jangan keseringan main game") # True
elif nilai == 'E' :
  print("keseringan bolos")
else :
  print("maaf, format nilai yang anda berikan tidak sesuai")
	
# switch case
# -----------
# dalam bahasa python tidak tersedia struktur switch case
# jadi untuk kondisi yang cukup banyak, kita harus menggunakan if elif else 
# atau menggunakan beberapa trik yang melibatkan function untuk pengganti switch case

# looping bersarang if
# --------------------
# looping bersarang adalah statement if yang didalamnya terdapat if lagi
# jika pernyataan if yang paling luar bernilai True, maka kondisi if yang didalam baru akan di cek

# contoh 
# ------
bekerja = True
umur = 25

if umur >= 25 : # True
  print("sudah dewasa")
  if bekerja : # True
    print("siap menikah")
  else :
    print("belum siap menikah")
else :
  print("masih bocah")
  if bekerja :
    print("tabung buat menikah")
  else :
    print("kerja dulu sana")

# short hand if
# -------------
# short hand if digunakan apabila hanya membutuhkan satu if tanpa elif atau else

# contoh
# ------
a = 7
b = 5

if (a > b) : print("{} lebih besar dari {}".format(a, b)) # True, 7 lebih besar dari 5
  
# short hand else
# ---------------
# else juga bisa dibuatkan short hand nya

# contoh
# ------
a = 18
b = 23

print("a lebih besar dari b") if (a > b) else print("a lebih kecil dari b") # a lebih kecil dari b

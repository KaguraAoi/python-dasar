# pengertian operand dan operator
# -------------------------------
# operand adalah nilai asal yang dipakai dalam sebuah proses operasi
# operator adalah instruksi yang diberikan untuk mendapatkan hasil dari proses tersebut

# contoh
# ------
# 10 + 2. angka 10 dan 2 adalah operand, sedangkan tanda tambah (+) adalah operator

# jenis-jenis operator dalam python
# ---------------------------------
# operator aritmatika
# operator perbandingan
# operator logika
# operator bitwise
# operator assignment
# operator identitas
# operator keanggotaan
# operator ternary

# operator aritmatika
# -------------------
# +, -, *, /, %, **

# contoh
# ------
a = 10
b = 2

# operator penjumlahan
c = a + b
print("hasil", a, " + ", b, " = ", c) # 12
# menggunakan operator sisa bagi
c = a % b
print("hasil", a, " % ", b, " = ", c) # 0
# menggunakan operator pangkat
c = a ** b
print("hasil", a, " ** ", b, " = ", c) # 100

# operator penugasan / assignment
# -------------------------------
# =
# operator assignment adalah operator untuk memasukkan suatu nilai ke dalam variabel
# operator assignment menggunakan tanda sama dengan (=)

# contoh
# ------
umur = 18 # variabel umur telah kita berikan tugas untuk menyimpan angka 18

# operator assignment gabungan
# ----------------------------
# operator assignment gabungan adalah penulisan singkat operator assignment yang digabung dengan dengan operator lain
# +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=
# misalnya a = a + 1 atau a += 1 (sama)

# contoh
# ------
a = 10
print("nilai a adalah ", a) # 10
# tambahkan dengan 2
a += 2 # a = 10 + 2
print("nilai a adalah ", a) # 12
# kurangi 3
a -= 3 # a = 12 - 3
print("nilai a adalah ", a) # 9

# operator pembanding
# -------------------
# operator ini digunakan untuk membandingkan dua buah nilai
# >, <, =, !=, >=, <=

# contoh
# ------
a = 9
b = 5
c = a == b # c = 9 == 5 ?
print ("apakah {} == {} : {}".format(a,b,c)) # False
c = a < b # c = 9 < 5 ?
print ("apakah {} == {} : {}".format(a,b,c)) # False
c = a > b # c = 9 > 5 ?
print ("apakah {} == {} : {}".format(a,b,c)) # True
c = a != b # c = 9 != 5 ?
print ("apakah {} == {} : {}".format(a,b,c)) # True

# operator logika
# ---------------
# operator logika digunakan untuk membuat operasi logika
# and, or, not
# cara hafal :
# and : dua dua harus True, selain itu False
# or : dua dua salah maka False, salah satu benar tetap True
# not : kebalikannya. misal not False maka True atau not True maka False 

# contoh
# ------
a = True
b = True
d = False
# logika AND
c = a and b
print("{} and {} = {}".format(a, b, c)) # True
# logika OR
c = a or d
print("{} and {} = {}".format(a, b, d)) # True
# logika NOT
c = not a
print("{} and {} = {}".format(a, b, c)) # False

# operator bitwise
# ----------------
# bitwise adalah operator khusus untuk menangani operasi logika bilangan biner dalam bentuk bit
# bilangan biner merupakan jenis bilangan yang hanya terdiri dari 2 jenis angka, yakni 0 dan 1
# jika nilai asal yang dipakai bukan bilangan biner, akan dikonversi menjadi bilangan biner
# misalnya 7 desimal == 0111 dalam bilangan biner
# &, |, ^, ~, <<, >>

# operator ternary
# ----------------
# operator ternary digunakan untuk membuat sebuah ekspresi
# kondisi seperti percabangan if/else

# contoh
# ------
# membuat operasi ternary menggunakann if/else dalam satu baris
umur = int(input("berapa umur kamu ? ")) # 18
aku = "bocah" if umur < 10 else "dewasa" # False maka dewasa
print (aku)

# urutan evaluasi
# ---------------
# urutan evaluasi merupakan urutan operator yang dikerjakan terlebih dahulu
# untuk urutan aritmatikanya yaitu KUKABATAKU (kurung, kali, bagi, tambah, kurang)

# mengubah urutan evaluasi
# ------------------------
# untuk membuat ekspresi lebih mudah dibaca, kita dapat menggunakan tanda kurung
# sebagai contoh, 2 + (3 * 4) lebih mudah dipahami daripada 2 + 3 * 4
# pemakaian tanda kurung jangan terlalu berlebihan seperti (2 + (3 * 4))

# contoh
# ------
hasil = 2 + 3 * 4
print ("2 + 3 * 4 = {}".format(hasil)) # 14
hasil = (2 + 3) * 4
print ("2 + 3) * 4 = {}".format(hasil)) # 20
hasil = 2 / 3 * 4
print ("2 / 3 * 4 = {}".format(hasil)) # 2,666...
hasil = 2.0 / 3 * 4
print ("2.0 / 3 * 4 = {}".format(hasil)) # 2,666...

# sifat asosiatif
# ---------------
# operator dengan level urutan evaluasi yang sama akan dievaluasi dari kiri ke kanan
# sebagai contoh 2 + 3 + 4 akan dievaluasi sebagai (2 + 3) + 4
# beberapa operator seperti pengisian nilai (assignment) mempunyai sifat asosiatif dari kanan ke kiri
# contoh: a = b = c akan dievaluasi a = (b = c)

# operator identitas dan keanggotaan
# ----------------------------------
# kedua operator ini kadang disebut juga sebagai operator khusus (special operator)
# operator ini tidak selalu tersedia di bahasa pemrograman lain

# operator identitas
# ------------------
# operator identitas adalah operator yang digunakan untuk memeriksa sebuah nilai,
# apakah nilai sebuah variabel ada di tempat yang sama (di memory) atau tidak
# operator ini terdiri dari 2 jenis: yaitu is dan is not
# is: bernilai True jika kedua operand merujuk ke object yang sama dan berisi nilai yang sama
# is not: bernilai True jika kedua operan merujuk ke objek yang tidak sama

# contoh
# ------
a = 5
b = 5
c = 6
print("a is b :", a is b) # True
print("a is c :", a is c) # False
print("a is not c :", a is not c) # True
i = "STMIK PONTIANAK"
j = "STMIK PONTIANAK"
print("i is j :", i is j) # False, meskipun nilai element-nya sama persis, 
# tapi python menyimpannya di alamat memory yang berbeda, sehingga dianggap tidak identik
print("i is not j :", i is not j) # True
x = ["a","b","c"]
y = ["a","b","c"]
print("x is y :", x is y) # False
print("x is not y :", x is not y) # True

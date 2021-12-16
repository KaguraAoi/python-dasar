# pengertian operand dan operator
# -------------------------------
# operand adalah nilai asal yang dipakai dalam sebuah proses operasi
# operator adalah instruksi yang diberikan untuk mendapatkan hasil dari proses tersebut

# contoh 
# 10 + 2. angka 10 dan 2 disebut sebagai operand, sedangkan tanda tambah (+) adalah operator

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
a = 10
b = 2

# menggunakan operator penjumlahan
c = a + b
print("hasil",a," + ",b," = ",c)
# menggunakan operator pengurangan
c = a - b
print("hasil",a," - ",b," = ",c)
# menggunakan operator perkalian
c = a * b
print("hasil",a," * ",b," = ",c)
# menggunakan operator pembagian
c = a / b
print("hasil",a," / ",b," = ",c)
# menggunakan operator sisa bagi
c = a % b
print("hasil",a," % ",b," = ",c)
# menggunakan operator pangkat
c = a ** b
print("hasil",a," ** ",b," = ",c)

# operator penugasan / assignment
# -------------------------------
# operator assignment adalah operator untuk memasukkan suatu nilai ke dalam variabel
# operator assignment menggunakan tanda sama dengan (=)
# +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=

# contoh
umur = 18 # variabel umur telah kita berikan tugas untuk menyimpan angka 18

# operator assignment gabungan
# ----------------------------
# operator assignment gabungan adalah cara penulisan singkat operator assignment yang digabung dengan dengan operator lain

# contoh
a += 1; # bisa disingkat (dan digabung) menjadi a += 1
# a = a + 1 atau a += 1 (sama)

# ambil suatu nilai
a = 10
print("nilai a adalah %d" % a) # 10
# tambahkan dengan 2
a += 2
print("nilai a adalah %d" % a) # 12
# kurangi 3
a -= 3
print("nilai a adalah %d" % a) # 9
# kali 10
a *= 10
print("nilai a adalah %d" % a) # 90
# bagi dengan 4
a /= 4
print("nilai a adalah %d" % a) # 22
# pangkat 10
a **= 2
# berapakah nilai a sekarang ?
print("nilai a adalah %d" % a) # 506

# operator pembanding
# -------------------
# operator ini digunakan untuk membandingkan dua buah nilai
# >, <, =, !=, >=, <=

# contoh
a = 9
b = 5
# apakah a sama dengan b?
c = a == b
print ("apakah %d == %d: %r" % (a,b,c)) # False
# apakah a < b?
c = a < b
print ("apakah %d < %d: %r" % (a,b,c)) # False
# apakah a > b?
c = a > b
print ("apakah %d > %d: %r" % (a,b,c)) # True
# apakah a <= b?
c = a <= b
print ("apakah %d <= %d: %r" % (a,b,c)) # False
# apakah a >= b?
c = a >= b
print ("apakah %d >= %d: %r" % (a,b,c)) # True
# apakah a != b?
c = a != b
print ("apakah %d != %d: %r" % (a,b,c)) # True

# operator logika
# ---------------
# operator logika digunakan untuk membuat operasi logika, seperti logika AND, OR, NOT
# and, or, not

# contoh
a = True
b = True
# logika AND
c = a and b
print("%r and %r = %r" % (a, b, c)) # True
# logika OR
c = a or b
print("%r or %r = %r" % (a, b, c)) # True
# logika NOT
c = not a
print("not %r = %r" % (a, c)) # False

# operator bitwise
# ----------------
# bitwise adalah operator khusus untuk menangani operasi logika bilangan biner dalam bentuk bit
# bilangan biner sendiri merupakan jenis bilangan yang hanya terdiri dari 2 jenis angka, yakni 0 dan 1. jika nilai asal yang dipakai bukan bilangan biner, akan dikonversi secara otomatis menjadi bilangan biner. misalnya 7 desimal = 0111 dalam bilangan biner
# Pada penerapannya, operator bitwise tidak terlalu sering dipakai, kecuali anda sedang membuat program yang harus memproses bit-bit komputer. selain itu operator ini cukup rumit dan harus memiliki pemahaman tentang sistem bilangan biner
# &, |, ^, ~, <<, >>

# contoh
a = 60
b = 13
# operasi AND
c = a & b
print ("a & b = %s" % c) # 12
# operasi OR
c = a | b
print ("a | b = %s" % c) # 61
# operasi XOR
c = a ^ b
print ("a ^ b = %s" % c) # 49
# operasi Not
c = ~a
print ("~a = %s" % c) # -61
# operasi shift left (tukar posisi biner) 
c = a << b
print ("a << b = %s" % c) # 491520
# operasi shift right (tukar posisi biner)
c = a >> b
print ("a >> b = %s" % c) # 0

# operator ternary
# ----------------
# operator ternary juga dikenal dengan operator kondisi, karena digunakan untuk membuat sebuah ekspresi
# kondisi seperti percabangan if/else

# contoh
# membuat operasi ternary menggunakann if/else dalam satu baris
umur = int(input("berapa umur kamu? ")) # 18
aku = "bocah" if umur < 10 else "dewasa" # False maka bocah
print (aku)

# membuat operasi ternary juga bisa menggunakan tuple dan list
jomblo = True
status = ("Menikah", "Single")[jomblo]
print (status)

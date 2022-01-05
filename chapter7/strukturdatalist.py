# konsep struktur data list
# -------------------------
# list adalah struktur data pada python yang mampu menyimpan lebih dari 1 data seperti array
# list merupakan struktur data terurut(sequence)
# setiap item dalam list memiliki indeks yang dimulai dari 0
# list direpresentasikan dengan karakter []
# list dalam python dapat menampung berbagai tipe data

# tipe data yang boleh diisi ke dalam list
# ----------------------------------------
# list dapat diisi dengan tipe data apa saja seperti string, int, float, dan sebagainya
# data list juga bisa dicampur isinya

# contoh
# ------
kotak = ["pisang", 50, True, 12.5]

# ada 4 tipe data pada list kotak yaitu :
# "pisang" adalah tipe data string
# 50 adalah tipe data int
# True adalah tipe data boolean
# 12.5 adalah tipe data float

# mengambil data dari list
# ------------------------
# kita menggunakan nomor indeks untuk mengambil isi(data) dari list
# nomor indeks selalu dimulai dari 0

# contoh 1
# --------
angka = [1, 2, 3, 4, 5]

print(angka) # dalam python jika ingin menampilkan semua isi dari list,
# cukup panggil nama list aja tanpa indeks

for a in angka :
  print(a) # 1 2 3 4 5

# contoh 2
# --------
buah = ["apel", "pisang", "mangga"]

# misal ingin mengambil data mangga
print(buah[2]) # mangga berada pada indeks ke 2

# contoh 3
# --------
temanku = ["budi", "sara", "ani"]

# menampilkan jumlah data dari list temanku
print("semua temanku berjumlah : {} orang".format(len(temanku))) # fungsi len,
# digunakan untuk menghitung jumlah data dalam list

# menampilkan data teman dari list temanku
for a in temanku :
  print(a) # budi sara ani

# mengganti nilai list
# --------------------
list bersifat mutable, artinya isinya bisa kita ubah

# contoh 1
# --------
buah = ["apel", "jeruk", "mangga"]

print(buah)

# misal kita bisa ubah mangga menjadi anggur
buah[2] = "anggur"

print(buah) # apel jeruk anggur

# contoh 2
# --------
angka = [3, 4, 5, 6]

print(angka) # 3 4 5 6
angka[2] = 10
print(angka) # 3 4 10 6

# negatif indeks
# --------------
# python memungkinkan pengindeksan negatif untuk urutannya,
# misalnya indeks -1 mengacu ke data terakhir dari list,
# -2 untuk item terakhir kedua dari list dan seterusnya

# contoh
# ------
my_list = ['a','p','e','l']

print(my_list[-1]) # l
print(my_list[-2]) # e
print(my_list[-3]) # p
print(my_list[-4]) # a
# pengertian variabel dan tipe data
# ---------------------------------
# variabel merupakan tempat menyimpan data
# tipe data adalah jenis data yang tersimpan dalam variabel
# variabel nilainya bisa berubah-ubah

# membuat variabel
# ----------------
# variabel di python dapat dibuat dengan format seperti ini:
# nama_variabel = [nilai]

# contoh
# ------
nilai_ujian = 87.5
nama = "Aditya"
lulus = False

# aturan penulisan variabel
# -------------------------
# nama variabel boleh diawali menggunakan huruf atau garis bawah (_), contoh: nama, _nama, namaKu, nama_variabel
# karakter selanjutnya dapat berupa huruf, garis bawah (_) atau angka, contoh: __nama, n2, nilai1
# karakter pada nama variabel bersifat case-sensitif. artinya huruf besar dan kecil dibedakan
# misalnya, variabel_Ku dan variabel_ku, keduanya adalah variabel yang berbeda
# nama variabel tidak boleh menggunakan kata kunci yang sudah ada dalam python seperti if, while, for, dsb

# tipe data
# ---------
# python akan secara otomatis mengenali tipe data yang tersimpan dalam sebuah variabel
# untuk memeriksa tipe data pada suatu variabel, kita bisa menggunakan fungsi type()

# contoh
# ------
jumlah = 2
ketelitian = 20.25
merk = "Xiao Mi"
print(type(jumlah))
print(type(ketelitian))
print(type(merk))

# jenis-jenis tipe data
# ---------------------
# Secara umum, tipe data primitif dalam python dibagi menjadi tiga jenis:
# tipe data angka
# tipe data teks
# tipe data boolan

# tipe data angka
# ---------------
# tipe data angka dibagi menjadi beberapa jenis lagi:
# integer, contoh 32, 22, 12, 10
# float, contoh 1.3, 4.2, 22.3

# contoh
# ------
harga = 120000000
berat = 23.12

# tipe data teks
# --------------
# tipe data teks dibagi menjadi dua jenis lagi:
# char, contoh 'R'
# string, contoh "aku lagi makan"
# penulisan tipe data teks harus diapit dengan tanda petik. bisa menggunakan petik tunggal(' ') atau ganda(" ")

# contoh
# ------
A = 'HP'
B = "SMARTPHONE ANDROID"

# tipe data boolean
# -----------------
# tipe data boolean adalah tipe data yang hanya memiliki dua nilai yaitu True dan False atau 0 dan 1
# penulisan True dan False, huruf pertamanya harus kapital dan tanpa tanda petik

# contoh
# ------
bergerak = False
nyala = 0

# konversi tipe data
# ------------------
# konversi digunakan apabila kita ingin mengubah suatu tipe data ke tipe data yang lain
# misalnya kita ingin mengubah input string menjadi int

# fungsi-fungsi untuk mengubah tipe data
# --------------------------------------
# int() untuk mengubah menjadi integer
# long() untuk mengubah menjadi integer panjang
# float() untuk mengubah menjadi float
# bool() untuk mengubah menjadi boolean
# chr() untuk mengubah menjadi karakter
# str() untuk mengubah menjadi string
# bin() untuk mengubah menjadi bilangan biner
# hex() untuk mengubah menjadi bilangan heksadesimal
# oct() untuk mengubah menjadi bilangan okta

# contoh
# ------
data = 212
st = str(data)
fl = float(data)
print(data, type(data))
print(st, type(st))
print(fl, type(fl))

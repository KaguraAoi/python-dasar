# konsep input output
# -------------------
# 1. input adalah masukan yang kita berikan ke program
# 2. program akan memprosesnya dan menampilkan hasil outputnya
# 3. input, proses, dan output adalah inti dari semua program komputer

# mengambil input dari keyboard
# -----------------------------
# fungsi input(): untuk mengambil inputan dari keyboard
# cara pakainya: nama_variabel = input("sebuah teks")

# contoh
# ------
nama = input("siapa nama kamu : ")
umur = input("berapa umur kamu : ")
print("hello", nama, "umur kamu adalah", umur, "tahun")

# menampilkan output
# ------------------
# untuk menampilkan output teks, kita menggunakan fungsi print()

# menampilkan variabel dan teks
# -----------------------------
# untuk menggabungkan teks dan variabel yang akan ditampilkan kita gunakan tanda koma (,)

# contoh
# ------
nama_variabel = "belajar python"
print("mari", nama_variabel) # mari belajar python

# menggabungkan teks dan variabel
# -------------------------------
# menggabungkan teks dan variabelnya dapat dengan menggunakan tanda plus (+)

# contoh
# ------
bhs = "python"
print("belajar " + bhs) # belajar python

# menggunakan fungsi format()
# ---------------------------
# fungsi format() akan menggabungkan isi variabel dengan teks
# tanda {} akan otomatis diganti sesuai dengan nilai yang kita inputkan ke variabel nama

# contoh
# ------
nama = input("nama anda : ")
buah = input("beli buah apa ? ")
print("{} , yuk belajar python".format(nama)) # andi, yuk belajar python
print("berarti {} makan buah {}".format(nama, buah)) # berarti andi makan buah pisang

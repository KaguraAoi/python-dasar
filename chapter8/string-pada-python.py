# karakter escape python
# ----------------------
# \a : bell atau alert
# \b : backspace/delete 1 karakter ke belakang
# \n : baris baru
# \t : spasi 4x

# contoh
# ------
print("saya \t belajar \t bahasa \t pemrograman")

# string built-in python
# ----------------------
# capitalize() : membuat huruf pertama string menjadi kapital
# upper() : membuat semua huruf pada string menjadi huruf besar
# lower() : membuat semua huruf pada string menjadi huruf kecil
# count() : menghitung berapa kali sebuah huruf pada string muncul
# center() : membuat string berada di tengah
# len() : mengukur panjang sebuah string
# find() : menentukan posisi sebuah huruf pada string
# replace() : mengganti sebuah substring lama dengan yang baru

# contoh
# ------
s = belajar PYTHON
print("kapital : ", s.capitalize()) # Belajar python
print("upper case : ", s.upper()) # BELAJAR PYTHON
print("lower case : ", s.lower()) # belajar python
print("jumlah huruf a : ", s.count('a')) # 2
print("posisi huruf P : ", s.lower('P')) # 8 (spasi dihitung)
print("posisi huruf o : ", s.lower('o')) # jika sebuah huruf,
# tidak tersedia di string maka akan mengembalikan nilai -1
print("panjang string : ", len(s)) # 14 (spasi dihitung)
print("belajar PYTHON ubah menjadi : ", s.replace("belajar", "kelas"))

# fungsi mumerik
# --------------
# abs() : merubah angka negatif menjadi positif
# min() : menentukan bilangan terkecil
# max() : menentukan bilangan terbesar
# pow() : menghitung bilangan berpangkat
# ceil() : membulatkan bilangan ke atas
# floor() : membulatkan bilangan ke bawah
# sqrt() : menghitung akar kuadrat
# choice() : mengacak item dari sebuah list
# randrange() : mengacak item dari sebuah list berdasarkan range

# contoh
# ------
# fungsi abs()
a = -2
b = -3.14

print(abs(a)) # 2
print(abs(b)) # 3.14

# fungsi min() dan max()
a = [2, 4, 6, 11, 3, 5]

print("nilai min : ", min(a)) # nilai min : 2
print("nilai max : ", max(a)) # nilai max : 11

# fungsi pow()
a = 3
b = 2

print(b, " pangkat ", a, " : ", pow(b, a)) # 2 pangkat 3 : 8

# fungsi ceil()
import math # harus import library math dahulu

a = 2.34
b = 3.67

print(math.ceil(a)) # harus ditulis math. dahulu, hasil : 3
print(math.ceil(b)) # 4

# fungsi floor()
import math

a = 2.34
b = 3.67

print(math.fllor(a)) # 2
print(math.floor(b)) # 3

# fungsi sqrt()
import math

a = 81

print(math.sqrt(a)) # 9.0

# fungsi choice()
import random # pakai library random

a = [2, 4, 6, 11, 3, 5]

print(random.choice(a)) # angka yang akan ditampilkan random (2/4/6/11/3/5)

# fungsi randrange()
import random

print(random.randrange(1, 30)) # mirip seperti choice tapi randrange mengacak,
# berdasarkan range misalnya range (1, 30) maka akan mengacak angka antara 1,
# sampai 30

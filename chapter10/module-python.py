# pengertian module
# -----------------
# module adalah kumpulan fungsi, class ataupun variabel

# cara membuat module
# -------------------
# 1. membuat file modul baru
# 2. nama file module adalah nama file python tersebut

# contoh
# ------
# nama module : luasBangunDatar
def luasPersegi(s) :
  return s * s
def luasPersegiPanjang(p, l) :
  return p * l
def luasSegitiga(a, t) :
  L = 0.5 * a * t
  return L

# secara defaulf, file luasBangunDatar memiliki ekstensi .pynb
# oleh karena itu, kita harus convert dahulu ke .py
# file module harus 1 folder dengan file yang ingin kita masukkan
# import-nya
# setelah membuat module maka kita bisa import ke file yang ingin
# digunakan import-nya. misal kita buat file baru bernama membuatModul

import luasBangunDatar

p = int(input("masukkan p : "))
l = int(input("masukkan l : "))
print("luas persegi panjang : ", luasBangunDatar.luasPersegiPanjang(p, l))
# luasBangunDatar adalah nama module-nya
# luasPersegiPanjang() adalah nama function yang ingin digunakan

# selain itu, kita juga bisa hanya mengambil fungsi secara spesifik dari module

from luasBangunDatar import luasPersegi

p = int(input("masukkan p : "))
l = int(input("masukkan l : "))
print("luas persegi panjang : ", luasPersegiPanjang(p, l))

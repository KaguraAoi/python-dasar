# perulangan / looping
# --------------------
# looping adalah instruksi kode program yang bertujuan untuk mengulang beberapa baris perintah
# dalam bahasa python, terdapat dua jenis looping yaitu for dan while

# konsep looping
# --------------
# looping dengan for biasanya digunakan untuk mengulangi kode yang jumlah perulangannya sudah diketahui
# looping dengan while terdapat syarat dan jumlah perulangannya tidak tentu,
# (tetap melakukan looping selama kondisi bernilai True)

# sintaks for
# -----------
for var in sequence :
  body of for
  
# var adalah nama variabel untuk menampung sementara nilai dari sequence pada saat terjadi looping
# sequence adalah tipe data berurutan seperti list, tuple atau array
# looping akan dilakukan sampai elemen terakhir dari sequence,
# bila sudah sampai ke elemen terakhir dari sequence, maka program akan keluar dari looping

# contoh 1
# --------
angka = [7, 8, 5, 3] # ini adalah sequence

for a in angka : # a adalah nama variabel sementara dan angka adalah sequence
  print(a) # 7 8 5 3

# contoh 2
# --------
item = ['kopi', 'jus', 'teh']

for isi in item :
  print(isi) # kopi jus teh
  
# fungsi range()
# --------------
# fungsi range() digunakan untuk menghasilkan deret bilangan
# misalkan range(10) maka akan menghasilkan bilangan dari 0 sampai dengan 9 (10 bilangan)
# kita juga bisa menentukan batas bawah, batas atas, dan interval,
# dengan format range(batas bawah, batas atas, interval)

# contoh
# ------
print(range(10)) # sama aja dengan range(0, 10), 0 adalah batas bawah sedangkan 10 adalah batas atasnya
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # kalo dibuat list maka batas atasnya,
# tidak termasuk list tetapi 1 angka dibawah batas atasnya
print(list(range(2,8))) # hasil: [2, 3, 4, 5, 6, 7]
print(list(range(2, 20, 3))) # hasil: [2, 5, 8, 11, 14, 17] # 3 adalah intervalnya (kelipatan dari
# deret bilangan)

# contoh 2
# --------
for i in range(0, 10, 2) :
  print(i) # 0 2 4 6 8
  
# contoh 3
# --------
ulang = 10

for i in range(ulang) :
  print("perulangan ke-" + str(i)) # perulangan ke-0 perulangan ke-... perulangan ke-9

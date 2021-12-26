# perulangan / looping
# --------------------
# perulangan adalah instruksi kode program yang bertujuan untuk mengulang beberapa baris perintah
# dalam bahasa python, terdapat dua jenis perulangan yaitu for dan while

# konsep perulangan
# -----------------
# perulangan dengan for biasanya digunakan untuk mengulangi kode yang jumlah perulangannya sudah diketahui
# perulangan dengan while terdapat syarat dan jumlah perulangannya tidak tentu (tetap melakukan looping selama kondisi bernilai True)

# sintaks for
# -----------

for var in sequence :
  body of for
  
# var adalah nama variabel yang digunakan untuk menampung sementara nilai dari sequence pada saat terjadi looping
# sequence adalah tipe data berurutan seperti list, tuple atau array
# looping akan dilakukan sampai elemen terakhir dari sequence. bila sudah sampai ke elemen terakhir dari sequence, maka program akan keluar dari looping

# contoh
# ------

angka = [7, 8, 5, 3] # ini adalah sequence

for a in angka : # a adalah variabel dan angka adalah sequence
  print(a)

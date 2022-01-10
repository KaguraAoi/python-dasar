# CRUD data mahasiswa sederhana

# ----
# LIST
# ----
mhs = []

# --------
# FUNCTION
# --------
def daftarmenu() :
    print("CRUD DATABASE MAHASISWA")
    print("---------------------------------")
    print("1. tambah data mahasiswa")
    print("2. tampilkan data mahasiswa")
    print("3. ubah data mahasiswa")
    print("4. hapus data mahasiswa")
    print("5. keluar program")
    print("---------------------------------")

# -----
# LOGIN
# -----
# username = 'AdityaAtha'
# password = 12345

# -----
# UTAMA
# -----
cekusername = input("masukkan username: ")
cekpassword = input("masukkan password: ")
print("---------------------------------")

if cekusername == 'AdityaAtha' and cekpassword == "12345" :
    daftarmenu()
    while(True) :
        pilih = int(input("masukkan pilihan: "))
        if pilih == 1 :
            namamhs = input("masukkan nama mahasiswa: ")
            mhs.append(namamhs)
        elif pilih == 2 :
            print(mhs)
        elif pilih == 5 :
            print("terimakasih telah menggunakan program ini")
            break
else :
    print("maaf, username atau password anda tidak sesuai")

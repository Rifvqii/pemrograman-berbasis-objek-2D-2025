class aksi:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print("data Mahasiswa:")
        print(f"nama     : {self.nama}")
        print(f"nim      : {self.nim}")
        print(f"jurusan  : {self.jurusan}")
        print(f"alamat   : {self.alamat}")


print("masukkan data mahasiswa 1:")
nama1 = input("nama: ")
nim1 = input("nim: ")
jurusan1 = input("prodi: ")
alamat1 = input("Alamat: ")
mahasiswa1 = aksi(nama1, nim1, jurusan1, alamat1)

print("masukkan data mahasiswa 2:")
nama2 = input("nama: ")
nim2 = input("nim: ")
jurusan2 = input("prodi: ")
alamat2 = input("alamat: ")
mahasiswa2 = aksi(nama2, nim2, jurusan2, alamat2)

print("masukkan data mahasiswa 3:")
nama3 = input("nama: ")
nim3 = input("nim: ")
jurusan3 = input("Prodi: ")
alamat3 = input("alamat: ")
mahasiswa3 = aksi(nama3, nim3, jurusan3, alamat3)

mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()
mahasiswa3.tampilkan_info()
# Class Induk
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")

# Class Anak 1 - Dosen (turunan dari Person)
class Dosen(Person):
    def __init__(self, nama, umur, nidn, mata_kuliah):
        super().__init__(nama, umur)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def tampilkan_info(self):
        print("=== Data Dosen ===")
        super().tampilkan_info()
        print(f"NIDN: {self.nidn}")
        print(f"Mata Kuliah: {self.mata_kuliah}")

    def mengajar(self):
        print(f"{self.nama} sedang mengajar mata kuliah {self.mata_kuliah}.\n")

# Class Anak 2 - Mahasiswa (turunan dari Person)
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim, jurusan):
        super().__init__(nama, umur)
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("=== Data Mahasiswa ===")
        super().tampilkan_info()
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")

    def belajar(self):
        print(f"{self.nama} sedang belajar di jurusan {self.jurusan}.\n")

# === Program Utama ===
# Data Dosen
dosen1 = Dosen("Edy", 30, "1512346", "Pemrograman Berorientasi Objek")
dosen1.tampilkan_info()
dosen1.mengajar()

# Data Mahasiswa
mhs1 = Mahasiswa("Khalid", 20, "24241142", "Pendidikan Teknologi Informasi")
mhs1.tampilkan_info()
mhs1.belajar()

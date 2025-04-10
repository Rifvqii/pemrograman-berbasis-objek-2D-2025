
class Hewan:
    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
    
    def bersuara(self):
        return f"{self.nama} mengeluarkan suara {self.suara}"

class Kucing(Hewan):
    def __init__(self, nama, warna):
        self.nama = nama
        self.jenis = "Kucing"
        self.suara = "Meong"
        self.warna = warna
    
    def info(self):
        return f"{self.nama} adalah kucing berwarna {self.warna}"

    def bersuara(self):
        return f"{self.nama} mengeluarkan suara {self.suara}"

class singa(Hewan):
    def __init__(self, nama, ras):
        self.nama = nama
        self.jenis = "singa"
        self.suara = "roarr"
        self.ras = ras

    def info(self):
        return f"{self.nama} adalah singa ras {self.ras}"

    def bersuara(self):
        return f"{self.nama} mengeluarkan suara {self.suara}"

class ayam(Hewan):
    def __init__(self, nama, bisa_terbang):
        self.nama = nama
        self.jenis = "ayam"
        self.suara = "petokok"
        self.bisa_terbang = bisa_terbang

    def info(self):
        kemampuan = "bisa terbang" if self.bisa_terbang else "tidak bisa terbang"
        return f"{self.nama} adalah ayam yang {kemampuan}"

    def bersuara(self):
        return f"{self.nama} mengeluarkan suara {self.suara}"


hewan_list = []
data_hewan = [
    ("irsyad", "hitam", "Kucing"),
    ("arza", "since", "singa"),
    ("anun", False, "ayam")
]

for data in data_hewan:
    if data[2] == "Kucing":
        hewan_list.append(Kucing(data[0], data[1]))
    elif data[2] == "singa":
        hewan_list.append(singa(data[0], data[1]))
    elif data[2] == "ayam":
        hewan_list.append(ayam(data[0], data[1]))

for hewan in hewan_list:
    print(hewan.info())
    print(hewan.bersuara())
    print()
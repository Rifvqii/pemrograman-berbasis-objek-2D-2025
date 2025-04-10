class orang:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} yang berusia {self.umur} tahun sedang berjalan di {self.alamat}")

    def berlari(self):
        print(f"{self.nama} yang berusia {self.umur} tahun sedang berlari di {self.alamat}")

irsyad = orang("irsyad", 18, "taman")
arza = orang("arza", 18, "depan rumah")
bima = orang("bima", 20, "belakang rumah")
kiki = orang("kiki", 18, "alun - alun")
rifki = orang("rifki", 17, "lapangan")

arza.berlari()
bima.berjalan()
irsyad.berjalan()
kiki.berlari()  
rifki.berjalan()
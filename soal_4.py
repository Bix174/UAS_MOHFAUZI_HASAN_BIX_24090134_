class Buah:
    def __init__(self):
        self.nama = ""
        self.warna = ""
        self.rasa = ""

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

jambu = Buah()
jambu.setNama("jambu")
jambu.setWarna("hijau")
jambu.setRasa("manis")

print("Nama Buah:", jambu.nama)
print("Warna Buah:", jambu.warna)
print("Rasa Buah:", jambu.rasa)

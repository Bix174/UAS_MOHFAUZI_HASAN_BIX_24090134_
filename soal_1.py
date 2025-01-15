data_mahasiswa = []

def inputan():
    mahasiswa = {}
    mahasiswa['nim'] = int(input('Masukan NIM : '))
    mahasiswa['nama'] = input('Masukan Nama  : ')
    data_mahasiswa.append(mahasiswa)
    
def tambah_input():
    inputan()
    tambah = input('ingin tambah lagi?(y/t) : ')
    if tambah == 'y':
        tambah_input()
    else:
        print(data_mahasiswa)

tambah_input()

import pandas as pd


data = {
    'Mahasiswa': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'algoritma  dan sruktur data 2': [80, 85, 90],
    'matematika numerik': [75, 85, 80],
    'Kimia': [85, 80, 85]
}


df = pd.DataFrame(data)


nilai_matakuliah = df[['algoritma dan sruktur data 2', 'matematika numerik', 'Kimia']].mean()
print("\nRata-rata nilai per mata kuliah:")
print(nilai_matakuliah)


nilai_mahasiswa = df[['algoritma dan sruktur data 2', 'matematika numerik', 'Kimia']].mean(axis=1)
print("\nRata-rata nilai per mahasiswa:")
for i, nilai_mahasiswa in (nilai_mahasiswa):
    print(f"{df['Mahasiswa'][i]}: {nilai_mahasiswa}")
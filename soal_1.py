while True:
  nama = input("Masukkan Nama : ")
  nim = input("Masukkan Nim : ")

  print ("Nama Mahasiswa" , nama , "Dengan NIM" , nim)

  perulangan = input("Apakah anda ingin melanjutkan? y/t?")

  if perulangan == "YA":
    continue
  elif perulangan == "TIDAK":
    print("terimakasih")
    break
  else:
      print("Maaf, inputan yang anda masukkan tidak sesuai!")
      perulangan = input("Apakah anda ingin melanjutkan? y/t?")
  if perulangan == "YA":
    continue
  elif perulangan == "TIDAK":
    print("Terima Kasih")
    break
def main():
    queue = RestaurantQueue()

    while True:
        print("Menu:")
        print("1. Tambah Pesanan")
        print("2. Hapus Pesanan")
        print("3. Tampilkan Antrean")
        print("4. Keluar")

        opsi = input("Pilih opsi: ")

        if opsi == "1":
            order = input("Masukkan nama pesanan : ")
            queue.enqueue(order)
        elif opsi == "2":
            queue.dequeue()
        elif opsi == "3":
            queue.display()
        elif opsi == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if _name_ == "main":
    main()
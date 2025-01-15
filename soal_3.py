class RestaurantQueue:
    def init(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Pesanan '{order}' berhasil ditambahkan ke antrian.")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Antrian kosong, tidak ada pesanan yang dapat dihapus.")
        else:
            removed_order = self.queue.pop(0)
            print(f"Pesanan '{removed_order}' telah dihapus dari antrian.")

    def display(self):
        if len(self.queue) == 0:
            print("Antrian kosong.")
        else:
            print("Antrian saat ini:")
            for i, order in enumerate(self.queue, start=1):
                print(f"{i}. {order}")
# Daftar untuk menyimpan data transaksi
daftar_transaksi = []

def tambah_transaksi(id_transaksi, id_produk, jumlah):
    """Menambahkan data transaksi ke dalam daftar."""
    transaksi = (id_transaksi, id_produk, jumlah)  # Membuat tuple untuk transaksi
    daftar_transaksi.append(transaksi)
    print(f'Transaksi ID "{id_transaksi}" telah ditambahkan.')

def tampilkan_transaksi():
    """Menampilkan semua data transaksi."""
    if daftar_transaksi:
        print("\nDaftar Transaksi:")
        for i, transaksi in enumerate(daftar_transaksi, 1):
            print(f"{i}. ID Transaksi: {transaksi[0]}, ID Produk: {transaksi[1]}, Jumlah: {transaksi[2]}")
    else:
        print("\nDaftar transaksi kosong.")

def main():
    """Fungsi utama untuk menjalankan program."""
    while True:
        print("\nMenu:")
        print("1. Tambah Transaksi")
        print("2. Lihat Daftar Transaksi")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            id_transaksi = input("Masukkan ID transaksi: ")
            id_produk = input("Masukkan ID produk: ")
            jumlah = int(input("Masukkan jumlah produk yang terjual: "))
            tambah_transaksi(id_transaksi, id_produk, jumlah)

        elif pilihan == "2":
            tampilkan_transaksi()

        elif pilihan == "3":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

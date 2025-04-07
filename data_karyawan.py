# Daftar untuk menyimpan data karyawan
daftar_karyawan = []

def tambah_karyawan(nama, id_karyawan, jabatan, gaji):
    """Menambahkan data karyawan ke dalam daftar."""
    karyawan = (nama, id_karyawan, jabatan, gaji)  # Membuat tuple untuk karyawan
    daftar_karyawan.append(karyawan)
    print(f'Data karyawan "{nama}" telah ditambahkan.')

def tampilkan_karyawan():
    """Menampilkan semua data karyawan."""
    if daftar_karyawan:
        print("\nDaftar Karyawan:")
        for i, karyawan in enumerate(daftar_karyawan, 1):
            print(f"{i}. Nama: {karyawan[0]}, ID: {karyawan[1]}, Jabatan: {karyawan[2]}, Gaji: {karyawan[3]}")
    else:
        print("\nDaftar karyawan kosong.")

def main():
    """Fungsi utama untuk menjalankan program."""
    while True:
        print("\nMenu:")
        print("1. Tambah Karyawan")
        print("2. Lihat Daftar Karyawan")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            nama = input("Masukkan nama karyawan: ")
            id_karyawan = input("Masukkan ID karyawan: ")
            jabatan = input("Masukkan jabatan karyawan: ")
            gaji = input("Masukkan gaji karyawan: ")
            tambah_karyawan(nama, id_karyawan, jabatan, gaji)

        elif pilihan == "2":
            tampilkan_karyawan()

        elif pilihan == "3":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

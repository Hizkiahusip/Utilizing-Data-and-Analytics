import csv

def tambah_pelanggan(nama, email, telepon):
    with open('database_pelanggan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, email, telepon])
    print("Data pelanggan berhasil ditambahkan.")

def cari_pelanggan(nama):
    with open('database_pelanggan.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == nama:
                return row
    return None

def hapus_pelanggan(nama):
    data = []
    with open('database_pelanggan.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != nama:
                data.append(row)
    
    with open('database_pelanggan.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Data pelanggan berhasil dihapus.")

def edit_pelanggan(nama, email, telepon):
    data = []
    with open('database_pelanggan.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == nama:
                row = [nama, email, telepon]
            data.append(row)
    
    with open('database_pelanggan.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Data pelanggan berhasil diupdate.")

def main():
    print("=== Program Data Entry Pelanggan ===")
    while True:
        print("\nPilih tindakan yang ingin dilakukan:")
        print("1. Tambah Pelanggan")
        print("2. Cari Pelanggan")
        print("3. Hapus Pelanggan")
        print("4. Edit Pelanggan")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            nama = input("Masukkan nama pelanggan: ")
            email = input("Masukkan email pelanggan: ")
            telepon = input("Masukkan nomor telepon pelanggan: ")
            tambah_pelanggan(nama, email, telepon)
        elif pilihan == '2':
            nama = input("Masukkan nama pelanggan yang ingin dicari: ")
            data = cari_pelanggan(nama)
            if data:
                print("Data Pelanggan:")
                print("Nama:", data[0])
                print("Email:", data[1])
                print("Telepon:", data[2])
            else:
                print("Data pelanggan tidak ditemukan.")
        elif pilihan == '3':
            nama = input("Masukkan nama pelanggan yang ingin dihapus: ")
            hapus_pelanggan(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama pelanggan yang ingin diupdate: ")
            email = input("Masukkan email baru pelanggan: ")
            telepon = input("Masukkan nomor telepon baru pelanggan: ")
            edit_pelanggan(nama, email, telepon)
        elif pilihan == '5':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-5.")

if __name__ == "__main__":
    main()

import csv

def tambah_pelanggan(nama, email, telepon):
    with open('database_pelanggan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, email, telepon])
    print("Data pelanggan berhasil ditambahkan.")

def main():
    print("=== Program Data Entry Pelanggan ===")
    while True:
        nama = input("Masukkan nama pelanggan: ")
        email = input("Masukkan email pelanggan: ")
        telepon = input("Masukkan nomor telepon pelanggan: ")
        
        # Validasi data
        if not nama or not email or not telepon:
            print("Error: Semua kolom harus diisi.")
            continue
        elif not email.count('@') == 1 or not email.count('.') >= 1:
            print("Error: Email tidak valid.")
            continue
        elif not telepon.isdigit() or len(telepon) < 10:
            print("Error: Nomor telepon tidak valid.")
            continue
        
        tambah_pelanggan(nama, email, telepon)
        
        lanjut = input("Apakah Anda ingin memasukkan data pelanggan lainnya? (y/n): ")
        if lanjut.lower() != 'y':
            break

if __name__ == "__main__":
    main()

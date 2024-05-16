import csv

def tambah_buku(judul, penulis, tahun_terbit, harga):
    with open('database_buku.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([judul, penulis, tahun_terbit, harga])
    print("Data buku berhasil ditambahkan.")

def main():
    print("=== Program Data Entry Toko Buku ===")
    while True:
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun_terbit = input("Masukkan tahun terbit: ")
        harga = input("Masukkan harga: ")
        
        # Validasi data
        if not judul or not penulis or not tahun_terbit or not harga:
            print("Error: Semua kolom harus diisi.")
            continue
        elif not tahun_terbit.isdigit() or not harga.replace('.', '').isdigit():
            print("Error: Tahun terbit dan harga harus dalam format angka.")
            continue
        
        tambah_buku(judul, penulis, tahun_terbit, harga)
        
        lanjut = input("Apakah Anda ingin memasukkan data buku lainnya? (y/n): ")
        if lanjut.lower() != 'y':
            break

if __name__ == "__main__":
    main()


"judul,penulis,tahun_terbit,harga"
"Python Programming,John Doe,2022,45.99"
"Data Science Handbook,Alice Smith,2020,39.95"
"Machine Learning Basics,Robert Johnson,2021,55.50"
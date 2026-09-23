produk = {}

def tambah_produk():
    nama = input("Masukkan nama: ")
    harga = float(input("Masukkan harga produk: "))
    
    if nama in produk:
        print("produk sudah ada!")
    else:
        produk[nama] = harga
        print("Produk berhasil ditambahkan.")
        
        
def lihat_produk():
    print("\n=== DAFTAR PRODUK ===")
    
    if not produk:
        print("Belum ada produk.")
        return
    
    for nama, harga in produk.items():
        print(f"Produk : {nama}")
        print(f"Harga : {harga}")
        print("-" * 25)
        
def update_produk():
        nama = input("Masukkan nama produk yang ingin diubah: ")
        
        if nama in produk:
            produk_baru = input("Masukkan Produk baru: ")
            produk[nama] = produk_baru
            print("produk berhasil diubah.")
        else:
            print("produk tidak ditemukan.")
        
def hapus_produk():
    nama = input("Masukkan nama produk yang ingin dihapus: ")
    
    if nama in produk:
        del produk[nama]
        print("produk berhasil dihapus.")
    else:
        print("produk tidak ditemukan.")
        
def hitung_total():
    nama = input("Masukkan nama produk: ")
    
    if nama not in produk:
        print("Produk tidak ditemukan")
        return
    
    jumlah = int(input("Masukkan Jumlah: "))
    
    harga = produk[nama]
    total = harga * jumlah 
    
    print("\n ===TOTAL BELANJA===")
    print(f"Produk : {nama}")
    print(f"Harga : Rp{harga:,.0f}")
    print(f"Jumlah : {jumlah}")
    print(f"Total : Rp{total:,.0f}")

def main():
    while True:
        print("\n=== PROGRAM KASIR SEDERHANA ===")
        print("1. Tambahkan Produk")
        print("2. Lihat Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Hitung Total Belanja")
        print("6. keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tambah_produk()
        if pilihan == "2":
            lihat_produk()
        if pilihan == "3":
            update_produk()
        if pilihan == "4":
            hapus_produk()
        if pilihan == "5":
            hitung_total()
        if pilihan == "6":
            print("Program selesai.")
            break
            

main()
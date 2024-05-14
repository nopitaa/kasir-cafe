#menu makanan yang tersedia
print("|==============================================|")
print("|         Mesin Kasir Cafe Cerita Kopi         |")
print("|==============================================|")
print("|              Pilih Menu Makanan              |")
print("| 1. Nasi Goreng                    Rp 25.000  |")
print("| 2. Mie Goreng Jawa                Rp 25.000  |")
print("| 3. Rice Bowl Chicken Teriyaki     Rp 30.000  |")
print("| 4. Rice Bowl Beef Bulgogi         Rp 35.000  |")
print("| 5. Rice Bowl Chicken Katsu Curry  Rp 30.000  |")
print("| 6. Pasta Aglio Olio               Rp 40.000  |")
print("|==============================================|")

# Inisialisasi total_makanan sebelum loop
total_makanan = 0
nama_makanan = ""
jumlah_porsi = 0

#terjadi looping,ketika pengguna memilih 0, program akan keluar dari loop dan melanjutkan ke baris berikutnya.
while True:
    menu_makanan = int(input("Pilih Menu (1-6) atau masukan 0 jika sudah selesai memilih: "))
    if menu_makanan == 0:
        break

    jumlah_porsi = int(input("Berapa Porsi :"))

    if menu_makanan == 1:
        harga = 25000
        nama_makanan = "Nasi Goreng"
    elif menu_makanan == 2:
        harga = 25000
        nama_makanan = "Mie Goreng Jawa"
    elif menu_makanan == 3:
        harga = 30000
        nama_makanan = "Rice Bowl Chicken Teriyaki"
    elif menu_makanan == 4:
        harga = 35000
        nama_makanan = "Rice Bowl Beef Bulgogi"
    elif menu_makanan == 5:
        harga = 30000
        nama_makanan = "Rice Bowl Chicken Katsu Curry"
    elif menu_makanan == 6:
        harga = 40000
        nama_makanan = "Pasta Aglio Olio"
    else:
        print("Pilihan tidak valid.")
        continue

    total_makanan += harga * jumlah_porsi
    print(nama_makanan, jumlah_porsi, "Porsi : Rp.", harga * jumlah_porsi)

#menu minuman yang tersedia
print()
print("|===============================|")
print("|      Pilih Menu Minuman       |")
print("|===============================|")
print("| 1. Hot Chocolate  Rp 30.000   |")
print("| 2. Frappuccino    Rp 40.000   |")
print("| 3. Macchiato      Rp 25.000   |")
print("| 4. Latte          Rp 30.000   |")
print("| 5. Matcha Latte   Rp 24.000   |")
print("|===============================|")

# Inisialisasi total_minum sebelum loop
total_minum = 0
nama_minuman = ""
jumlah_gelas = 0

#terjadi looping,ketika pengguna memilih 0, program akan keluar dari loop dan melanjutkan ke baris berikutnya.
while True:
    menu_minuman = int(input("Pilih Menu (1-4) atau masukan 0 jika sudah selesai memilih: "))
    if menu_minuman == 0:
        break

    jumlah_gelas = int(input("Berapa Gelas :"))

    if menu_minuman == 1:
        harga_minuman = 30000
        nama_minuman = "Hot Chocolate"
    elif menu_minuman == 2:
        harga_minuman = 40000
        nama_minuman = "Frappuccino"
    elif menu_minuman == 3:
        harga_minuman = 25000
        nama_minuman = "Macchiato"
    elif menu_minuman == 4:
        harga_minuman = 30000
        nama_minuman = "Latte"
    elif menu_minuman == 5:
        harga_minuman = 24000
        nama_minuman = "Matcha Latte"
    else:
        print("Pilihan tidak valid.")
        continue
#Menghitung total harga semua minuman yang di pesan
    total_minum += harga_minuman * jumlah_gelas
    print(nama_minuman, jumlah_gelas, "Gelas : Rp.", harga_minuman * jumlah_gelas)

#proses menghitung semua harga yang harus di bayar
jumlah_semua = total_makanan + total_minum

#struk menampilkan semua total yang harus di bayarkan
print()
print("|===============================|")
print("|        Struk Pembelian        |")
print("|===============================|")
print("|Makanan :", nama_makanan,"\t        |")
print("|Porsi   :", jumlah_porsi,"\t\t\t|")
print("|Minuman :", nama_minuman,"\t        |")
print("|Porsi   :", jumlah_gelas,"\t\t\t|")
print("|===============================|")
print("|   Total Yang Harus Di Bayar   |")
print("|===============================|")
print("|Total   :", jumlah_semua,"               |")
print("|===============================|")
print()
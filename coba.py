#suhu air
suhu_air = float(input("Masukkan suhu air dalam Celcius: "))

if suhu_air <= 0:
    print("Air berada dalam wujud padat (es)")
elif suhu_air < 100:
    print("Air berada dalam wujud cair")
else:
    print("Air berada dalam wujud gas (uap)")

#bilangan bulat
bilangan = int(input("Masukan Bilangan: "))
if(bilangan % 2 == 0):
    print("Bilangan ", bilangan ," adalah bilangan genap")
else:
    print("Bilangan ", bilangan ," adalah bilangan ganjil")
    
#inputan karakter
huruf = ("Masukan karakter huruf:")
if huruf in ('a', 'e', 'i', 'o', 'u'):
    print(f"{huruf} adalah huruf vokal.")
else:
    print(f"{huruf} bukan huruf vokal.")

#kode pos
#pengguna untuk memasukkan nama kota melalui input
nama_kota = input("Masukkan nama kota: ")

if nama_kota == "Padang":
    print("Kode pos untuk kota Padang adalah: 25000")
elif nama_kota == "Bandung":
    print("Kode pos untuk kota Bandung adalah: 40100")
elif nama_kota == "Solo":
    print("Kode pos untuk kota Solo adalah: 51000")
elif nama_kota == "Denpasar":
    print("Kode pos untuk kota Denpasar adalah: 72000")
elif nama_kota == "Palu":
    print("Kode pos untuk kota Palu adalah: 92300")
else:
    print("Kota tidak ditemukan dalam daftar.")
    
#upah karyawan
# suhu air
suhu_air = float(input("Masukkan suhu air dalam Celcius: "))

if suhu_air <= 0:
    print("Air berada dalam wujud padat (es)")
elif suhu_air < 100:
    print("Air berada dalam wujud cair")
else:
    print("Air berada dalam wujud gas (uap)")

# bilangan bulat
bilangan = int(input("Masukkan Bilangan: "))
if bilangan % 2 == 0:
    print("Bilangan", bilangan ,"adalah bilangan genap")
else:
    print("Bilangan", bilangan ,"adalah bilangan ganjil")

# inputan karakter
huruf = input("Masukkan karakter huruf: ")
if huruf in ('a', 'e', 'i', 'o', 'u'):
    print(f"{huruf} adalah huruf vokal.")
else:
    print(f"{huruf} bukan huruf vokal.")

# kode pos
# pengguna untuk memasukkan nama kota melalui input
nama_kota = input("Masukkan nama kota: ")

if nama_kota == "Padang":
    print("Kode pos untuk kota Padang adalah: 25000")
elif nama_kota == "Bandung":
    print("Kode pos untuk kota Bandung adalah: 40100")
elif nama_kota == "Solo":
    print("Kode pos untuk kota Solo adalah: 51000")
elif nama_kota == "Denpasar":
    print("Kode pos untuk kota Denpasar adalah: 72000")
elif nama_kota == "Palu":
    print("Kode pos untuk kota Palu adalah: 92300")
else:
    print("Kota tidak ditemukan dalam daftar.")

# upah karyawan
def hitung_upah(jam_kerja):
    upah_per_jam = 2000.0
    upah_lembur_per_jam = 3000.0
    jam_lembur = 0

    if jam_kerja > 48:
        jam_lembur = jam_kerja - 48
        jam_kerja = 48

    upah_pokok = jam_kerja * upah_per_jam
    upah_lembur = jam_lembur * upah_lembur_per_jam
    upah_total = upah_pokok + upah_lembur

    return upah_total

jam_kerja = float(input("Masukkan jumlah jam kerja: "))
upah_mingguan = hitung_upah(jam_kerja)

print("Upah mingguan karyawan:", upah_mingguan)



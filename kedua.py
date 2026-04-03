#input
hari_total = int(input("Masukkan jumlah hari proyek: "))

#proses
tahun = hari_total // 365
sisa = hari_total % 365

bulan = sisa // 30
hari = sisa % 30

#output
print("Hasil konversi:")
print(tahun, "tahun,", bulan, "bulan,", hari, "hari")
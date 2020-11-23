# Konversi detik ke dalam jam menit dan detik

nilai = input("detik : ")
satuan = 60
detik = int(nilai)

hari = int(detik / (satuan * satuan * 24))
detik = int(detik - (satuan * satuan * 24) * hari)

jam = int(detik / (satuan * satuan))
detik = int(detik - (satuan * satuan) * jam)

menit = int(detik / satuan)
detik = int(detik - (satuan * menit))

print(f" H:j:m:d => {hari}:{jam}:{menit}:{detik}")

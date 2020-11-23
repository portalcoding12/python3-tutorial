# Program sederhana menentukan zodiak cina berdasarkan tahun lahir

zodiak = ['tikus','kerbau','macan','kelinci','naga','ular','kuda','kambing','monyet','ayam','anjing','babi']
tahun = int(input("Tahun lahir anda : "))
hasil = (tahun - 4) % 12
if hasil <= 11:
    print(f"tahun {tahun}, zodiak cina anda adalah {zodiak[hasil]}")
else:
    print("zodiak tidak ditemukan")

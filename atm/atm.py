# PROGRAM ATM SEDERHANA MENGGUNAKAN BAHASA PEMROGRAMAN PYTHON
pin = '123456'
saldo = 0

print('Selamat Datang di program ATM, BANK PORTAL CODiNG')

for i in range(3):
    print()
    inPin = input("Silahkan masukkan 6 digit pin anda : ")
    if inPin == pin :
        print()
        print("PIN yang Anda masukkan benar")
        print()
        break

    else :
        print("PIN salah")
        if i == 2 :
            print("============================================")
            print("Akun anda kami tangguhkan selama 24 jam")
            print("============================================")
            quit()

pilihan = 'y'
while (pilihan == 'y'):
    print('01. Silahkan pilih 1 untuk informasi saldo')
    print('02. Silahkan pilih 2 untuk penarkan uang tunai')
    print('03. Silahkan pilih 3 untuk setor tabungan')
    print('04. Silahkan pilih 4 untuk keluar')
    print()

    menu = input('Silahkan pilih menu yang anda inginkan : ')
    print("===================================================")

    if menu == '1':
        print(f"Sisa saldo anda : {saldo}")
    elif menu == '2':

        if saldo < 50000:
            print("Maaf, saldo anda tidak mencukupi.")
            print("Silahkan isi saldo terlebih dahulu.")

        else:
            print("Jumlah nominal penarikan sebesar 50000, 100000, 250000, 500000, 1000000")
            tunai = int(input("Jumlah penarikan anda : "))
            if (tunai == 50000) or (tunai == 100000) or (tunai == 250000) or (tunai == 500000) or (tunai == 1000000):
                saldo == saldo - tunai
                print()
                print(f"Saldo ditarik : {tunai}")
                print(f"Sisa saldo anda : {saldo}")
            else:
                print("Nominal tidak diketahui")

    elif menu == '3':
        setor = int(input("Silahkan masukkan nominal yang ingin di setor : "))
        saldo = saldo + setor
        print()
        print(f"Sisa saldo anda : {saldo}")

    elif menu == '4':
        print("Kartu anda akan keluar dari mesin ATM")
        print()
        print("Terima kasih sudah menggunakan layanan BANK PORTAL CODING")
        print()

    print("=========================================================")
    pilihan = input("Apakah ingin melanjutkan program (y/n)? ")
    print("=========================================================")

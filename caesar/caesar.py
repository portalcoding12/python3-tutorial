# Membuat program enkripsi dan dekripsi caesar menggunakan python 3

# Rumus Enkripsi : (n - key) % 26
# Rumus Dekripsi : (n + key) % 26
#
# n = merupakan urutan dari abjad yang diinput
# key = merupakan kunci dekripsi atau enkripsi nya
# 26 = merupakan jumlah dari seluruh abjad

print("----------------------+ Program Enkripsi Caesar +----------------------")

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# abjad berfungsi untuk menampung nilai abjad yang ada

# fungsi enkripsi dengan parameter abjad
def enkripsi(abjad):
    str = input("String : ") #input string yang akan di enkripsi
    key = int(input("Key : ")) #kunci untuk pergeseran abjad (enkripsi)

    str = str.lower() #string dikonversi ke huruf kecil semua
    result = '' #deklarasi variable result dengan nilai awal adalah kosong

    for char in str: #membuat perulangan untuk pergeseran abjad dari string
        if char in abjad: #abjad string dipecah 1 1 dan di cek apakah terdapat dalam value abjad
            n = abjad.index(char) #jika ada maka nilai index dari abjad yang ditemukan disimpan dalam variable n
            encrypt = (n - key) % 26 #rumus enkripsi
            convert = abjad[encrypt] #konversi nilai string ke hasil enkripsi
            result = result + convert #abjad yang sudah di konversi disimpat dalam variable result dalam bentuk string
        else:
            result = result + ' ' #jika abjad dari string tidak ditemukan dalam index abjad, maka akan dirubah ke dalam
                                  # bentuk spasi

    print(f"Result : {result}") #hasil dari perulangan untuk enkripsi string di tampilkan


#fungsi dekripsi dengan parameter abjad
def dekripsi(abjad):
    str = input("String Enkripsi : ") #input string yang akan di dekripsi
    key = int(input("Key : ")) #kunci untuk pergeseran abjad (dekripsi)

    str = str.lower() #string dikonversi ke huruf kecil semua
    result = '' #deklarasi variable result dengan nilai awal adalah kosong

    for char in str: #membuat perulangan untuk pergeseran abjad dari string
        if char in abjad: #abjad string dipecah 1 1 dan di cek apakah terdapat dalam value abjad
            n = abjad.index(char) #jika ada maka nilai index dari abjad yang ditemukan disimpan dalam variable n
            encrypt = (n + key) % 26 #rumus enkripsi
            convert = abjad[encrypt] #konversi nilai string ke hasil dekripsi
            result = result + convert #abjad yang sudah di konversi disimpat dalam variable result dalam bentuk string
        else:
            result = result + ' ' #jika abjad dari string tidak ditemukan dalam index abjad, maka akan dirubah ke dalam
                                  # bentuk spasi

    print(f"Result : {result}") #hasil dari perulangan untuk enkripsi string di tampilkan


# pembuatan menu
pilihan = 'y'

while (pilihan == 'y'):
    print("Menu yang tersedia : ")
    print("01. Enkripsi Data")
    print("02. Dekripsi Data")
    print("03. Keluar")

    menu = input("Menu yang dipilih : ")
    print("-------------------------------------")

    if menu == '1':
        print("Menu Enkripsi Data")
        enkripsi(abjad)
    elif menu == '2':
        print("Menu Dekripsi Data")
        dekripsi(abjad)
    elif menu == '3':
        print("Program Selesai, terima kasih.")
        break
    else:
        print("Menu tidak ditemukan")


    print("------------------------------------")
    pilihan = input("Apakah ingin melanjutkan ? (Y/n) : ")
    print("------------------------------------")

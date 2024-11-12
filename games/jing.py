import random

def start():

    while True:
        jingpy_pss = random.randint(1, 4)

        kolom = "|o|"
        kolom_kosong = [kolom] * 4
        kolom_jingpy = kolom_kosong.copy()

        kolom_jingpy[jingpy_pss - 1] = "|×͜×|"

        kolom_kosong = ' '.join(kolom_kosong)
        kolom_jingpy = ' '.join(kolom_jingpy)
        print(f'Coba perhatikan kolom ini: \n\n{kolom_kosong}\n')

        pilihan = int(input("dikolom nomor berapa jingpy berada? [1/2/3/4] "))
        while(pilihan > 4 or pilihan < 1):
            pilihan = int(input("isi kolomnya dengan benar, silahkan pilih nomor 1-4? "))

        if pilihan == jingpy_pss:
            print(f"{kolom_jingpy} \nselamat pilihanmu benar.")
        else:
            print(f"{kolom_jingpy} \nsayang sekali pilihanmu salah.")
        print("")
        ulang = input("apakah kamu mau lanjut main (y/n)? ")    
        if ulang == "n":
            break
        else:
            print('baiklah kalo mau lanjut!! coba perhatikan lagi kolom dibawah.')

    print("\nterimakasih telah memainkan game ini")

def kalkulator():
    while True:
        angka1 = int(input("masukkan angka pertama: "))
        angka2 = int(input("masukkan angka kedua: "))
        menu = int(input("pilih menu: \n1. penjumlahan \n2. pengurangan \n3. perkalian \n4. pembagian \n> "))
        if menu == 1:
            print(f"hasil penjumlahan {angka1} + {angka2} = {angka1 + angka2}")
        elif menu == 2:
            print(f"hasil pengurangan {angka1} - {angka2} = {angka1 - angka2}")
        elif menu == 3:
            print(f"hasil perkalian {angka1} x {angka2} = {angka1 * angka2}")
        elif menu == 4:
            print(f"hasil pembagian {angka1} / {angka2} = {angka1 / angka2}")
        else:
            print("menu tidak tersedia silahkan ulangi kembali")
        ulang = input("apakah kamu mau lanjut main (y/n)? ")    
        if ulang == "n":
            break
    print("\nterimakasih telah memainkan game ini")
    

if __name__ == "__main__" :
    start()
    kalkulator()
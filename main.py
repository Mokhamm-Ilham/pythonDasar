from lib import welcome
from games import jing

def main():
    welcome("WELCOME TO JINGPY AWOKAWOK")
    pilihan = int(input('Pilih menu yang akan digunakan: \n1. JINGPY \n2. KALKULATOR \n> '))
    if pilihan == 1:
        jing.start()
    elif pilihan == 2:
        jing.kalkulator()
    else:
        print("menu tidak tersedia silahkan ulangi kembali")

if __name__ == "__main__" :
    main()
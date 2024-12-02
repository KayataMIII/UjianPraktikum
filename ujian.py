def updatestok():
    dm_ml_10 = 100 #10 diamond ml 
    dm_ml_100 = 100 #100 diamond ml
    dm_ml_500 = 100 #500 diamond ml
    dm_ml_1000 = 100 #1000 diamond ml
    token_hok_100 = 100 #Token HOK 100
    token_hok_300 = 100 #Token HOK 300
    token_hok_600 = 100 #Token HOK 600
    token_hok_1000 = 100 #Token HOK 1000
    return dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100 , token_hok_300, token_hok_600, token_hok_1000


def show_games(dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100,token_hok_300, token_hok_600, token_hok_1000):
    print("""
=====Daftar Game=====
1. Mobile Legends
2. Honor Of Kings
3. Keluar  
""")
    opsi = int(input("Pilih Game: "))
    if opsi == 1:
        print("==============Games Mobile Legends==============")
        print(f"1. Harga 10 Diamond     :Rp 5000, Stok Tersedia     : {dm_ml_10} ")
        print(f"2. Harga 100 Diamond    :Rp 70000, Stok Tersedia    : {dm_ml_100} ")
        print(f"3. Harga 500 Diamond    :Rp 300000, Stok Tersedia   : {dm_ml_500} ")
        print(f"4. Harga 1000 Diamond   :Rp 500000, Stok Tersedia   : {dm_ml_1000} ")
        print ("="*65)
    
    elif opsi == 2:
        print("==============Games Honor Of Kings==============")
        print(f"1. Harga 100 Token      :Rp 20000, Stok Tersedia     : {token_hok_100} ")
        print(f"1. Harga 300 Token      :Rp 50000, Stok Tersedia     : {token_hok_300} ")
        print(f"2. Harga 600 Token      :Rp 150000, Stok Tersedia    : {token_hok_600} ")
        print(f"3. Harga 1000 Token     :Rp 300000, Stok Tersedia    : {token_hok_1000} ")
        print ("="*65)
    
    elif opsi == 3:
        return()
    
    return opsi

def total():
    total_harga = 0
    qty_item = 0

    return total_harga, qty_item

def top_up(dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100 , token_hok_300, token_hok_600, token_hok_1000, total_harga, total_belanja, qty_item, opsi):
    while True:
        show_games(dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100 , token_hok_300, token_hok_600, token_hok_1000)

        if opsi == 1:
            transaksi = input("Ingin Beli Opsi berapa (1-4): ")
            if transaksi == '1':
                dm_ml_10 -= 1
                total_harga += 5000
                qty_item += 1
                print("Anda telah Membeli 10 Diamond Mobile Legends, Terimakasih!!")

            elif transaksi == '2':
                dm_ml_100 -= 1
                total_harga += 70000
                qty_item += 1
                print("Anda telah Membeli 100 Diamond Mobile Legends, Terimakasih!!")

            elif transaksi == '3':
                dm_ml_500 -= 1
                total_harga += 300000
                qty_item += 1
                print("Anda telah Membeli 500 Diamond Mobile Legends, Terimakasih!!")

            elif transaksi == '4':
                dm_ml_1000 -= 1
                total_harga += 5000000
                qty_item += 1
                print("Anda telah Membeli 1000 Diamond Mobile Legends, Terimakasih!!")

        elif opsi == 2:
            transaksi = input("Ingin Beli Opsi berapa (1-4): ")
            if transaksi == '1':
                token_hok_100 -= 1
                total_harga += 20000
                qty_item += 1
                print("Anda telah Membeli 100 Token HoK, Terimakasih!!")

            elif transaksi == '2':
                token_hok_300 -= 1
                total_harga += 50000
                qty_item += 1
                print("Anda telah Membeli 300 Token HoK, Terimakasih!!")

            elif transaksi == '3':
                token_hok_600 -= 1
                total_harga += 150000
                qty_item += 1
                print("Anda telah Membeli 600 Token HoK, Terimakasih!!")

            elif transaksi == '4':
                token_hok_1000 -= 1
                total_harga += 300000
                qty_item += 1
                print("Anda telah Membeli 1000 Token Hok, Terimakasih!!")

        elif opsi == 0:
            print ("Wkwkwkw")
    
        return dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100 , token_hok_300, token_hok_600, token_hok_1000, total_harga, total_belanja, qty_item

def print_receipt(total_harga, qty_item):
    try:
        with open("transaksi.txt", "w") as ts:
            ts.write(f"==================Receipt==================")
            ts.write(f"Total Harga  Anda      : {total_harga}")
            ts.write(f"Total Belanja Anda     : {qty_item} Items")
        

    except Exception as e:
        print(e)


def main():
    dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100, token_hok_300, token_hok_600, token_hok_1000 = updatestok()
    total_harga, total_belanja, qty_item = total()
    opsi = 0
    nama = input("Masukkan Username anda: ")
    print(f'====Selamat Datang {nama}====')
    print("======Aplikasi EzStoreKuy======")
    while True:
        print("""
Daftar Menu:
1. Daftar Games
2. Top Up Games
3. Cetak Transaksi
4. Keluar
""")
        menu = input("Pilih menu (1-4): ")
        if menu == '1':
            show_games(dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100 , token_hok_300, token_hok_600, token_hok_1000)

        elif menu == '2':
            dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100 , token_hok_300, token_hok_600, token_hok_1000, total_harga, qty_item, opsi = top_up(opsi,dm_ml_10, dm_ml_100, dm_ml_500, dm_ml_1000, token_hok_100 , token_hok_300, token_hok_600, token_hok_1000, total_harga, total_belanja, qty_item)

        elif menu == '3':
            print_receipt(total_harga, qty_item)
        elif menu == '4':
            break

if __name__ == "__main__":
    main()

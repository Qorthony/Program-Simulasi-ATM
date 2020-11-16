nasabah = [{'no.rek': '12121212', 'nama': 'anjay', 'pin':
            '13131313', 'bank': 'mandiri', 'saldo': 5000000},
           {'no.rek': '14141414', 'nama': 'suja', 'pin':
            '15151515', 'bank': 'mandiri', 'saldo': 4000000},
           {'no.rek': '16161616', 'nama': 'bangjago', 'pin':
            '17171717', 'bank': 'bri', 'saldo': 3000000}]

login_status = False
current_login = ""


def login():
    print("please insert your id")
    print("---------------------")
    rekening = input("no rekening :")
    pin = input("pin :")

    cek_rek = False
    for i in nasabah:
        if i['no.rek'] == rekening:
            cek_rek = True

    cek_pin = False
    for i in nasabah:
        if i['pin'] == pin:
            cek_pin = True

    if (cek_rek and cek_pin):
        global current_login
        current_login = rekening
        print("\nBerhasil\n")
        return True
    else:
        print("\nGagal\n")
        return False


def logout():
    global login_status, current_login
    login_status = False
    current_login = ""


def menu_bank():
    print("\n\nmenu Transaksi")
    print("-------------------")
    print("1. Lihat saldo")
    print("2. Tarik Tunai")
    print("3. Transfer Tunai")
    print("4. Ubah Password")
    print("5. Keluar")
    print("-------------------")


def lihat_saldo():
    for i in nasabah:
        if i["no.rek"] == current_login:
            saldo = i["saldo"]
    print("Saldo anda : ", saldo)


def get_one_nasabah(no_rek):
    for i in nasabah:
        if i["no.rek"] == no_rek:
            data_nasabah = i
    return data_nasabah


def transfer_tunai():
    nominal = int(input("Masukkan nominal transaksi :"))
    rek = input("Masukkan no rekening tujuan : ")

    nasabah_pengirim = get_one_nasabah(current_login)
    nasabah_tujuan = get_one_nasabah(rek)
    biaya_admin = 0

    print("Data nasabah tujuan")
    print("===================")
    print("No rek :", nasabah_tujuan["no.rek"])
    print("Nama : ", nasabah_tujuan["nama"])
    print("Bank : ", nasabah_tujuan["bank"])
    print("--------------------")
    print("Nominal : ", nominal)

    if (nasabah_pengirim["bank"] == nasabah_tujuan["bank"]):
        print("Biaya admin : ", biaya_admin)
    else:
        biaya_admin = 6500
        print("Biaya admin : ", biaya_admin)
    print("----------------------")

    pin = input("masukkan pin anda : ")
    if pin==nasabah_pengirim["pin"]:
        i=0
        for n in nasabah:
            if n["no.rek"]==nasabah_pengirim["no.rek"]:
                key_nasabah_pengirim = i
            i+=1
        
        saldo_update_pengirim = nasabah[key_nasabah_pengirim]["saldo"]-nominal-biaya_admin
        nasabah[key_nasabah_pengirim].update({"saldo":saldo_update_pengirim})

        i=0
        for n in nasabah:
            if n["no.rek"]==nasabah_tujuan["no.rek"]:
                key_nasabah_tujuan = i
            i+=1
        saldo_update_tujuan = nasabah[key_nasabah_tujuan]["saldo"]+nominal
        nasabah[key_nasabah_tujuan].update({"saldo":saldo_update_tujuan})

        print("Transaksi berhasil")
    else:
        print("Transaksi Gagal")
                

while True:
    if login_status == False:
        login_status = login()

    else:
        menu_bank()
        pilihan = input("pilihan (1..4):")
        if (pilihan == "1"):
            lihat_saldo()
        elif (pilihan == "2"):
            print("")
        elif (pilihan == "3"):
            transfer_tunai()
        elif (pilihan == "4"):
            print("")
        elif (pilihan == "5"):
            logout()
            print("\n anda telah logout \n")

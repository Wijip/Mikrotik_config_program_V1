import os, logging
from ip_calculator import IP_Calculator

def show_menu(id):
    if id == 0: # MAIN MENU
        print("================================================================")
        print('= 1. IP Kalkulator                                             =')
        print("= 2. Konfigurasi                                               =")
        print("= 0. Exit                                                      =")
        print("================================================================")
    elif id == 1:  #KONFIGURASI LAYER 1
        print("================================================================")
        print("=                      MENU KONFIGURASI                        =")
        print("================================================================")
        print("= 1. interface                                                 =")
        print("= 2. PPP                                                       =")
        print("= 3. IP                                                        =")
        print("= 4. Queue                                                     =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif id == 2: # KONFIGURASI -> INTERFACE
        print("================================================================")
        print("=                  KONFIGURASI INTERFACE                       =")
        print("================================================================")
        print("= 1. bridge                                                    =")
        print("= 2. ethernet                                                  =")
        print("= 3. wireless                                                  =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif id == 3: # KONFIGURASI -> PPP
        print("================================================================")
        print("=                     KONFIGURASI PPP                          =")
        print("================================================================")
        print("= 1. bridge                                                    =")
        print("= 2. ethernet                                                  =")
        print("= 3. wireless                                                  =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif id == 4: # KONFIGURASI -> IP
        print("================================================================")
        print("=                     KONFIGURASI IP                           =")
        print("================================================================")
        print("= 1. address                                                   =")
        print("= 2. dhcp-client                                               =")
        print("= 3. wireless                                                  =")
        print("= 0. Back                                                      =")
        print("================================================================")
    else:
        print("================================================================")
        print("=                  KONFIGURASI QUEUE                           =")
        print("================================================================")
        print("= 1. DUMMY                                                     =")
        print("= 2. DUMMY                                                     =")
        print("= 0. Back                                                      =")
        print("================================================================")


def wait_for_input():
    input("Tekan Enter untuk melanjutkan...")


def main():
    id = 0
    logging.basicConfig(filename='IP_Calculator.log', level=logging.INFO)

    while True:
        os.system('cls')
        show_menu(id)
        pilih = input("Masukkan Pilihan : ")
        if pilih.isdigit():
            pilih = int(pilih)
            if id == 0:
                if pilih == 1:
                    ip_address = input("Masukkan IP Address (Ex : 192.168.1.1) : ")
                    cidr = int(input("Masukkan Subnet(CIDR) range 8 - 32 : "))

                    if not 8 < cidr < 32:
                        print("Error : Angka CIDR yang diinputkan melebihi angka 32 atau kurang dari angka 8")
                        logging.error("Error: Angka yang diinput melebihi angka 32 atau kurang dari angka 8")
                    else:
                        calculator = IP_Calculator()
                        subnet_mask = calculator.cidr_to_subnet(cidr)
                        network = calculator.network_address(ip_address, subnet_mask)
                        broadcast = calculator.broadcast_address(network, subnet_mask)
                        usable_ip = calculator.usable_range(network, broadcast)

                        ip_info = [
                            ['IP Address            : ',ip_address],
                            ['Subnet Mask           : ',subnet_mask],
                            ['Network Address       : ',network],
                            ['Broadcast             : ',broadcast],
                            ['Usable Rang           : ',usable_ip]
                        ]

                        for row in ip_info:
                            print('{:<20} {}'.format(row[0], row[1]))
                            logging.info(row[0] + ' ' + row[1])
                    wait_for_input()
                elif pilih == 2:
                    id += 1
                elif pilih == 0:
                    break
            elif id == 1:
                if 1 <= pilih <= 4:
                    id += pilih
                elif pilih == 0:
                    id -= 1
            elif id == 2:
                if pilih == 1:
                    print("KONFIGURASI -> INTERFACE -> BRIDGE")
                    wait_for_input()
                elif pilih == 2:
                    print("KONFIGURASI -> INTERFACE -> ETHERNET")
                    wait_for_input()
                elif pilih == 3:
                    print("KONFIGURASI -> INTERFACE -> WIRELESS")
                    wait_for_input()
            elif id == 3:
                if pilih == 1:
                    print("KONFIGURASI -> PPP -> BRIDGE")
                    wait_for_input()
                elif pilih == 2:
                    print("KONFIGURASI -> PPP -> ETHERNET")
                    wait_for_input()
                elif pilih == 3:
                    print("KONFIGURASI -> PPP -> WIRELESS")
                    wait_for_input()
            elif id == 4:
                if pilih == 1:
                    print("KONFIGURASI -> IP -> ADDRESS")
                    wait_for_input()
                elif pilih == 2:
                    print("KONFIGURASI -> IP -> DHCP-CLIENT")
                    wait_for_input()
                elif pilih == 3:
                    print("KONFIGURASI -> IP -> WIRELESS")
                    wait_for_input()
            elif id == 5:
                if pilih == 1:
                    print("KONFIGURASI -> QUEUE -> DUMMY1")
                    wait_for_input()
                elif pilih == 2:
                    print("KONFIGURASI -> QUEUE -> DUMMY2")
                    wait_for_input()
            if pilih == 0 and id > 1:
                id = 1


if __name__ == "__main__":
    main()

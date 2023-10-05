import logging
from mikrotik_connection import MikrotikConnection
from manual_config import Manual_config
from ip_calculator import IP_Calculator

def show_menu(index):
    if index == 0: # MAIN MENU
        print("================================================================")
        print('= 1. IP Kalkulator                                             =')
        print("= 2. Konfigurasi                                               =")
        print("= 0. Exit                                                      =")
        print("================================================================")
    elif index == 1:  #KONFIGURASI LAYER 1
        print("================================================================")
        print("=                      MENU KONFIGURASI                        =")
        print("================================================================")
        print("= 1. interface                                                 =")
        print("= 2. PPP                                                       =")
        print("= 3. IP                                                        =")
        print("= 4. Queue                                                     =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif index == 2: # KONFIGURASI -> INTERFACE
        print("================================================================")
        print("=                  KONFIGURASI INTERFACE                       =")
        print("================================================================")
        print("= 1. bridge                                                    =")
        print("= 2. ethernet                                                  =")
        print("= 3. wireless                                                  =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif index == 3: # KONFIGURASI -> PPP
        print("================================================================")
        print("=                     KONFIGURASI PPP                          =")
        print("================================================================")
        print("= 1. bridge                                                    =")
        print("= 2. ethernet                                                  =")
        print("= 3. wireless                                                  =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif index == 4: # KONFIGURASI -> IP
        print("================================================================")
        print("=                     KONFIGURASI IP                           =")
        print("================================================================")
        print("= 1. address                                                   =")
        print("= 2. dhcp-client                                               =")
        print("= 3. wireless                                                  =")
        print("= 0. Back                                                      =")
        print("================================================================")

    else: # KONFIGURASI -> QUEUE
        print()


def main():
    logging.basicConfig(filename='IP_Calculator.log', level=logging.INFO)
    index = 0
    pilih = -1
    while pilih != 0 and index != 0:
        show_menu(index)
        pilih = int(input("Masukkan Pilihan : "))
        if pilih == 1:
            ip_address = input("Masukkan IP Address (Ex : 192.168.1.1) : ")
            cidr = int(input("Masukkan Subnet(CIDR) range 8 - 32 : "))

            if cidr > 32 or cidr < 8:
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
                    ['Usabel Rang           : ',usable_ip]
                ]

                for row in ip_info:
                    print('{:<20} {}'.format(row[0], row[1]))
                    logging.info(row[0] + ' ' + row[1])
                input("Tekan enter")


if __name__ == '__main__':
    main()

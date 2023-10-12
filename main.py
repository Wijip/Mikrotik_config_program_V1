import os, logging
import time

from ip_calculator import IP_Calculator
from  manual_config import Manual_config
from mikrotik_connection import MikrotikConnection


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
        print("= 2. IP                                                        =")
        print("= 3. Queue                                                     =")
        print("= 4. Firwall                                                   =")
        print("= 5. bridge                                                    =")
        print("= 6. hotspot                                                   =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif index == 2: # KONFIGURASI -> INTERFACE
        print("================================================================")
        print("=                  KONFIGURASI INTERFACE                       =")
        print("================================================================")
        print("= 1. create bridge                                             =")
        print("= 2. ethernet                                                  =")
        print("= 3. wireless                                                  =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif index == 3: # KONFIGURASI -> IP
        print("================================================================")
        print("=                     KONFIGURASI IP                           =")
        print("================================================================")
        print("= 1. address                                                   =")
        print("= 2. dhcp-client                                               =")
        print("= 3. wireless                                                  =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif index == 4:# KONFIGURASI QUEUE
        print("================================================================")
        print("=                  KONFIGURASI QUEUE                           =")
        print("================================================================")
        print("= 1. DUMMY                                                     =")
        print("= 2. DUMMY                                                     =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif index == 5:# KONFIGURASI FIREWALL
        print("================================================================")
        print("=                  KONFIGURASI FIREWALL                        =")
        print("================================================================")
        print("= 1. DUMMY                                                     =")
        print("= 2. DUMMY                                                     =")
        print("= 0. Back                                                      =")
        print("================================================================")
    elif index == 6:
        print("================================================================")
        print("=                  KONFIGURASI BRIDGE                          =")
        print("================================================================")
        print("= 1. Create Bridge Interface                                   =")
        print("= 2. Add port to bridge                                        =")
        print("= 0. Back                                                      =")
        print("================================================================")
    else:
        print("================================================================")
        print("=                  KONFIGURASI HOTSPOT                         =")
        print("================================================================")
        print("= 1. DUMMY hotspot                                             =")
        print("= 2. DUMMY hotspot                                             =")
        print("= 0. Back                                                      =")
        print("================================================================")


def wait_for_input():
    input("Tekan Enter untuk melanjutkan...")


def main():
    index = 0
    logging.basicConfig(filename='IP_Calculator.log', level=logging.INFO)
    while True:
        os.system('cls')
        show_menu(index)
        pilih = input("Masukkan Pilihan : ")
        if pilih.isdigit():
            pilih = int(pilih)
            if index == 0:
                if pilih == 1:
                    ip_address = input("Masukkan IP Address (Ex : 192.168.1.1) : ")
                    cidr = int(input("Masukkan Subnet(CIDR) range 8 - 32 : "))
                    if not 8 < cidr < 32:
                        print("Error : Angka CIDR atau subnet yang diinputkan melebihi angka 32 atau dibawah angka 8")
                        logging.error("Error: Angka yang diinputkan melebihi 32 atau dibawah angka 8")
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
                    hostname = input("IP Address Router Mikrotik : ")
                    username = input("Username : ")
                    password = input("Password : ")
                    connection = MikrotikConnection(hostname, username, password)
                    if connection.connect():
                        time.sleep(2)
                        index += 1
                    else:
                        print("Login Gagal!!!")
                        time.sleep(3)
                elif pilih == 0:
                    break
            elif index == 1:
                if 1 <= pilih <= 6:
                    index += pilih
                elif pilih == 0:
                    connection.close_connection()
                    print("closing connection")
                    time.sleep(1)
                    index -= 1
            elif index == 2:
                if pilih == 1:
                    print("Create Bridge")
                    wait_for_input()
                elif pilih == 2:
                    print("KONFIGURASI -> INTERFACE -> ETHERNET")
                    wait_for_input()
                elif pilih == 3:
                    print("KONFIGURASI -> INTERFACE -> WIRELESS")
                    wait_for_input()
            elif index == 3:
                if pilih == 1:
                    manual_configuration = Manual_config(connection)
                    print("KONFIGURASI -> IP -> ADDRESS")
                    interface = input("Masukkan nama interface (Ex ether1) : ")
                    ip_address = input("Masukkan IP Address : ")
                    subnet_mask = input("Masukkan Subnet range 8 - 32 : ")
                    result = manual_configuration.configure_ip(interface, ip_address, subnet_mask)
                    wait_for_input()
                elif pilih == 2:
                    print("KONFIGURASI -> IP -> DHCP-CLIENT")
                    wait_for_input()
                elif pilih == 3:
                    print("KONFIGURASI -> IP -> WIRELESS")
                    wait_for_input()
            elif index == 4:
                if pilih == 1:
                    print("KONFIGURASI -> QUEUE -> DUMMY1")
                    wait_for_input()
                elif pilih == 2:
                    print("KONFIGURASI -> QUEUE -> DUMMY2")
                    wait_for_input()
            elif index == 5:
                if pilih == 1:
                    print("Dummy Firewall 1")
                    wait_for_input()
                elif pilih == 2:
                    print("Dummy Firewall 2")
                    wait_for_input()
            elif index == 6:
                if pilih == 1:
                    manual_configuration = Manual_config(connection)
                    print("Create bridge interface")
                    name_bridge = input("Masukkan nama interface bridge : ")
                    result = manual_configuration.create_bridge(name_bridge)
                    wait_for_input()
                elif pilih == 2:
                    print("add port to bridge")
                    name_bridge = input("Masukkan nama interface bridge : ")
                    interface = input("Masukkan interface yang akan ditambahkan : ")
                    result = manual_configuration.add_bridge_port(name_bridge,interface)
                    wait_for_input()
            elif index == 7:
                if pilih == 1:
                    print("Dummy Hotspot 1")
                    wait_for_input()
                elif pilih == 2:
                    print("Dummy hotspot 2")
                    wait_for_input()
            if pilih == 0 and index > 1:
                index = 1


if __name__ == "__main__":
    main()

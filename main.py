import logging, time
from mikrotik_connection import MikrotikConnection
from manual_config import Manual_config
from ip_calculator import IP_Calculator

def main():
    logging.basicConfig(filename='IP_Calculator.log', level=logging.INFO)
    while True:
        print("================================================================")
        print('= 1. IP Kalkulator                                             =')
        print("= 2. Konfigurasi                                               =")
        print("= 3. Exit                                                      =")
        print("================================================================")

        pilih = int(input("Masukkan Pilihan 1/2/3 : "))
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
                    ['Usabel Rang           : ',usable_ip]
                ]

                for row in ip_info:
                    print('{:<20} {}'.format(row[0], row[1]))
                    logging.info(row[0] + ' ' + row[1])
                input("Tekan enter")
        elif pilih == 2:
            hostname = input("IP Address Router Mikrotik : ")
            username = input("Username : ")
            password = input("Password : ")

            connection = MikrotikConnection(hostname, username, password)
            if connection.connect():
                # print("Login berhasil!!!\n")
                manual_config = Manual_config(connection)
                print("================================================================")
                print("=                      MENU KONFIGURASI                        =")
                print("================================================================")
                print("= 1. interface                                                 =")
                print("= 2. PPP                                                       =")
                print("= 3. IP                                                        =")
                print("= 4. Queue                                                     =")
                print("================================================================")
                pilih = int(input("Masukkan Pilihan konfigurasi : "))
                if pilih == 1:
                    print("================================================================")
                    print("=                  KONFIGURASI INTERFACE                       =")
                    print("================================================================")
                    print("= 1. bridge                                                    =")
                    print("= 2. ethernet                                                  =")
                    print("= 3. wireless                                                  =")
                    print("================================================================")

                elif pilih == 2:
                    print("================================================================")
                    print("=                     KONFIGURASI PPP                          =")
                    print("================================================================")
                    print("= 1. bridge                                                    =")
                    print("= 2. ethernet                                                  =")
                    print("= 3. wireless                                                  =")
                    print("================================================================")

                elif pilih == 3:
                    print("================================================================")
                    print("=                     KONFIGURASI IP                           =")
                    print("================================================================")
                    print("= 1. address                                                   =")
                    print("= 2. dhcp-client                                               =")
                    print("= 3. wireless                                                  =")
                    print("================================================================")
                    pilih = int(input("Pilih konfigurasi : "))

                    if pilih == 1:
                        interface = input("Masukkan nama Interface : ")
                        ip_address = input("Masukkan alamat IP : ")
                        subnet_mask = input("Masukkan subnet mask : ")
                        result = manual_config.configure_ip(interface, ip_address, subnet_mask)
                        # print(result)
                        time.sleep(1)
                        # connection.close_connection()

            else:
                print("Login Gagal")
                break
        elif pilih == 3:
            break


if __name__ == '__main__':
    main()

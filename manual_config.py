class Manual_config:
    def __init__(self, mikrotik_connection):
        self.connection = mikrotik_connection

    def Change_Interface_Name(self, interface, new_name):
        command = f'/interface set {interface} name={new_name}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi kesalahan",str(e))
        else:
            print(f"Interface {interface} berhasil dirubah menjadi {new_name}")

    def Create_Bridge(self,name_bridge):
        command = f'/interface bridge add fast-forward=no name={name_bridge}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            print(f"Interface bridge berhasil dibuat dengan nama {name_bridge}")

    def Add_Bridge_Port(self, name_bridge, interface):
        jumlah = int(input("Masukkan berapa port yang akan dimasukkan dalam interface bridge :"))
        for i in range(jumlah):
            command = f'/interface bridge port add bridge={name_bridge} interface={interface}'
            try:
                result = self.connection.execute_command(command)
            except Exception as e:
                print("Terjadi Kesalahan",str(e))
            else:
                print(f"Interface {interface} berhasil ditambahkan di bridge {name_bridge}")


    def Configure_IP(self, interface, ip_address, subnet_mask):
        command = f'/ip address add interface={interface} address={ip_address}/{subnet_mask}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            print(f"IP Address {ip_address}/{subnet_mask} berhasil ditambahkan diinteface {interface}")

    def DHCP_Client(self,interface):
        command = f'/ip dhcp-client add disable=no interface={interface}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan:",str(e))
        else:
            print(f"DHCP Client berhasil diterapkan di interface {interface}")

    def IP_POOL(self, pool_name, ranges):
        command = f'/ip pool add name={pool_name} ranges={ranges}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print(f"IP Pool berhasil ditambahkan dengan nama {pool_name} dengan ranges {ranges}")

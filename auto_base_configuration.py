class auto_base_configuration:
    def __init__(self, mikrotik_connectino):
        self.connection = mikrotik_connectino

    def auto_base_ip_configuration(self):
        command = f'/ip address add interface=ether2 address=192.168.100.1/24'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            print(f'IP Address berhasil ditambahkan')

    def auto_base_dhcp_client(self):
        command = f'/ip dhcp-client add disable=no interface=ether1'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            print("DHCP CLient berhasil ditambahkan")

    def auto_base_ip_pool(self):
        command = f'/ip pool add name=pool1 ranges=192.168.100.2-192.168.100.254'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan", str(e))
        else:
            print("IP Pool berhasil ditambahkan")

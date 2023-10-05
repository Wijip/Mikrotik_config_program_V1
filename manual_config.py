class Manual_config:
    def __init__(self, mikrotik_connection):
        self.connection = mikrotik_connection

    def configure_ip(self, interface, ip_address, subnet_mask):
        command = f'/ip address add interface={interface} address={ip_address}/{subnet_mask}'

        try:
            result = self.connection.execute_command(command)


        except Exception as e:
            print("Terjadi Kesalahan",str(e))


        else:
            print(f"IP Address {ip_address}/{subnet_mask} berhasil ditambahkan diinteface {interface}")

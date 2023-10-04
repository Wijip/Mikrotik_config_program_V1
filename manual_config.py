class Manual_config:
    def __init__(self, mikrotik_connection):
        self.connection = mikrotik_connection

    def configure_ip(self, interface, ip_address, subnet_mask):
        try:
            command = f'/ip address add interface={interface} address={ip_address}/{subnet_mask}'
            stdin, stdout, stderr = self.connection.exec_command(command)
            error = stderr.read().decode()
            if not error:
                print(f"IP address {ip_address}/{subnet_mask} berhasil ditambahkan pada interface {interface}")
            else:
                print("terjadi kesalahan:",error)
        except Exception as e:
            print('terjadi kesalahan', str(e))


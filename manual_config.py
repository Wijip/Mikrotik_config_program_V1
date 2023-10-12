class Manual_config:
    def __init__(self, mikrotik_connection):
        self.connection = mikrotik_connection

    def change_interface_name(self, interface, new_name):
        command = f'/interface set {interface} name={new_name}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi kesalahan",str(e))
        else:
            if not result:
                print(f"Interface {interface} berhasil dirubah menjadi {new_name}")
            else:
                print(result)

    def create_bridge(self,name_bridge):
        command = f'/interface bridge add fast-forward=no name={name_bridge}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            if not result:
                print(f"Interface bridge berhasil dibuat dengan nama {name_bridge}")
            else:
                print(result)

    def add_bridge_port(self, name_bridge, interface):
        jumlah = int(input("Masukkan berapa port yang akan dimasukkan dalam interface bridge :"))
        for i in range(jumlah):
            command = f'/interface bridge port add bridge={name_bridge} interface={interface}'
            try:
                result = self.connection.execute_command(command)
            except Exception as e:
                print("Terjadi Kesalahan",str(e))
            else:
                print(f"Interface {interface} berhasil ditambahkan di bridge {name_bridge}")

    def configure_ip(self, interface, ip_address, subnet_mask):
        command = f'/ip address add interface={interface} address={ip_address}/{subnet_mask}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            # print(result)
            if not result:
                print(f"IP Address {ip_address}/{subnet_mask} berhasil ditambahkan diinteface {interface}")
            else:
                print(result)
    def configure_dns(self, server):
        command = f'/ip dns set servers={server} allow-remote-requests=yes'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            print(f"DNS berhasil ditambahkan dengan DNS Server {server}")

    def dhcp_client(self,interface):
        command = f'/ip dhcp-client add disable=no interface={interface}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan:",str(e))
        else:
            print(f"DHCP Client berhasil diterapkan di interface {interface}")

    def configure_ip_pool(self, pool_name, ranges):
        command = f'/ip pool add name={pool_name} ranges={ranges}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print(f"IP Pool berhasil ditambahkan dengan nama {pool_name} dengan ranges {ranges}")

    def dhcp_server(self, pool_name, interface, name_dhcp):
        command = f'/ip dhcp-server add address-pool={pool_name} disabled=no interface={interface} lease-time=1h name={name_dhcp}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            print(f"DHCP Server berhasil ditambahkan dengan nama {name_dhcp} dan menggunakan pool {pool_name}")

    def configure_dhcp_network(self,network_address, gateway):
        command = f'/ip dhcp-server network add address={network_address} gateway={gateway}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terkjadi Kesalahan",str(e))
        else:
            print(f'DHCP Network berhasil ditambahkan dengan network address {network_address}\nserta gateway address {gateway}')

    def masquerade_nat(self, src_address):
        command = f'/ip firewall nat add action=masquerade chain=srcnat src-address={src_address}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            print(f"Firewall Nat Maquerade dapat ditambahkan dengan src-address:{src_address}")

    def configure_firewall_raw(self, action, address_list, address_list_timeout,chain, comment, content, dst_address_list, src_address_list):
        command = f'/ip firewall raw add action={action} address-list={address_list} address-list-timeout={address_list_timeout} chain={chain} comment={comment} content={content} dst-address-list={dst_address_list} src-address-list={src_address_list}'
        try:
            result = self.connection.execute_command(command)
        except Exception as e:
            print("Terjadi Kesalahan",str(e))
        else:
            print(f'Firewall RAW berhasil ditambahkan untuk Konten {content}')

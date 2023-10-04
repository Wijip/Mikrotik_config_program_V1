class IP_Calculator:
    @staticmethod
    def cidr_to_subnet(cidr):
        subnet = ''
        for i in range(4):
            if cidr >= 8:
                subnet += '255.'
                cidr -= 8
            else:
                subnet += str(256 - 2**(8-cidr)) + '.'
                cidr = 0
        return subnet[:-1]

    @staticmethod
    def network_address(ip, subnet):
        network = ''
        ip_parts = ip.split('.')
        subnet_parts = subnet.split('.')
        for i in range(4):
            network += str(int(ip_parts[i]) & int(subnet_parts[i])) + '.'
        return network[:-1]

    @staticmethod
    def broadcast_address(network, subnet):
        broadcast = ''
        network_parts = network.split('.')
        subnet_parts = subnet.split('.')
        for i in range(4):
            broadcast += str(int(network_parts[i]) | (255 - int(subnet_parts[i]))) + '.'
        return broadcast[:-1]

    @staticmethod
    def usable_range(network, broadcast):
        network_parts = network.split('.')
        broadcast_parts = broadcast.split('.')
        network_parts[-1] = str(int(network_parts[-1]) + 1)
        broadcast_parts[-1] = str(int(broadcast_parts[-1]) - 1)
        return '.'.join(network_parts) + ' - ' + '.'.join(broadcast_parts)

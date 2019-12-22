import math
import scapy.config

def skip_interface(network, netmask, iface, address):
    return network==0 or iface=='lo' or address=='127.0.0.1' or address=='0.0.0.0' or netmask<=0 or netmask==0xFFFFFFFF or iface.startswith('docker')

def long2net(netmask):
    if (netmask <= 0 or netmask >= 0xFFFFFFFF):
        raise ValueError('illegal netmask value', hex(netmask))
    return 32 - int(round(math.log(0xFFFFFFFF - netmask, 2)))

def to_CIDR_notation(network, netmask):
    network = scapy.utils.ltoa(network)
    netmask = long2net(netmask)
    net = f'{network}/{netmask}'
    if netmask < 16:
        return None

    return net

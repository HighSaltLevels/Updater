from time import sleep
import socket
import scapy.config
import scapy.layers.l2
import scapy.route
import errno
import exceptions
import network_tools
from log import LOGGER

# This code was taken from https://github.com/bwaldvogel/neighbourhood/blob/master/neighbourhood.py
def get_ips():
    ips = []
    for network, netmask, _, iface, address, _ in scapy.config.conf.route.routes:
        if not network_tools.skip_interface(network, netmask, iface, address):
            try:
                network = network_tools.to_CIDR_notation(network, netmask)
                if not network.startswith('169'):
                    ans, unans = scapy.layers.l2.arping(network, iface=iface, timeout=5)
                    for _, r in ans.res:
                        ips.append(r.psrc)
            except socket.error as error:
                if error.errno == errno.EPERM:
                    LOGGER.error('Operation not permitted')
                    raise exceptions.OperationNotPermittedException(error)
            except Exception as error:
                raise exceptions.GetHostnamesException('Unexpected Error: {}'.format(error))
        sleep(0.1)
    ips.sort()
    LOGGER.info('Found IP addresses: {}'.format(ips))
    return ips

def update_pc(ip):
    pass

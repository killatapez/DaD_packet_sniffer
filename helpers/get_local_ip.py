import socket
import psutil
import sys

def get_local_ip(interface_name):
    for interface, addrs in psutil.net_if_addrs().items():
        if interface == interface_name:
            for addr in addrs:
                if addr.family == socket.AF_INET:  # IPv4 address
                    return addr.address
    return None

sys.modules[__name__] = get_local_ip
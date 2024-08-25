import pyshark
import struct
import os

from helpers import get_local_ip, parse_all, log, messageMap

def capture_packets(interface='Ethernet', port_range=(20200, 20300)):
    local_ip = get_local_ip(interface)
    if not local_ip:
        print(f"Could not find IP address for interface {interface}")
        return

    dispFilter = (f'ip.dst == {local_ip} '
                  f'and tcp.srcport >= {port_range[0]} '
                  f'and tcp.srcport <= {port_range[1]} '
                  f'and tcp.payload > 1')
    print(dispFilter)
    packet_data = b""
    try:
        capture = pyshark.LiveCapture(interface=interface, display_filter=dispFilter)

        for packet in capture.sniff_continuously():
            if (packet.tcp.payload.binary_value[:4] == b'\x08\x00\x00\x00'):
                packet_length, proto_type, random_padding = struct.unpack('<IHH', packet.tcp.payload.binary_value[:8])
                print(list(messageMap.keys())[list(messageMap.values()).index(proto_type)])
                continue

            payload = packet.tcp.payload.binary_value
            packet_length, proto_type, random_padding = struct.unpack('<IHH', payload[:8])

            if len(payload) == packet_length:
                parse_all(payload, proto_type, packet_length)
                continue

            with open(f'{os.getcwd()}\\logs_server\\buffer.txt', 'a+') as file:
                file.write(payload.hex())
            packet_data += payload
            packet_length, proto_type, random_padding = struct.unpack('<IHH', packet_data[:8])

            if len(packet_data) >= packet_length:
                if parse_all(packet_data, proto_type, packet_length):
                    packet_data = packet_data[packet_length:]

                    log(str(packet.sniff_time), 'logs_server', packet_data)
                    with open(f'{os.getcwd()}\\logs_server\\buffer.txt', 'w+') as file:
                        file.write(packet_data[packet_length:].hex())
                else:
                    log(str(packet.sniff_time)+'_failed', 'logs_server', packet_data)

    except Exception as e:
        raise e

    
if __name__ == "__main__":
    print('These are the server-side packets\n')
    capture_packets()
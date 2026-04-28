from scapy.all import ARP, Ether, srp

def scan_devices(ip_range="192.168.1.1/24"):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []

    for sent, received in result:
        devices.append({
            "IP": received.psrc,
            "MAC": received.hwsrc
        })

    return devices
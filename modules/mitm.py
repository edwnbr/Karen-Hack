import random
from .utils import print_slow

def intercept(ip):
    print_slow(f"Starting MITM attack on {ip}...")
    for _ in range(10):
        pkt = "".join(random.choice("0123456789ABCDEF") for _ in range(24))
        print_slow(f"  Intercepted packet: {pkt}")
    print_slow("MITM channel established.")

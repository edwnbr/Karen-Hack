import random
from .utils import print_slow

def scan(ip):
    print_slow(f"Scanning {ip}...")
    for _ in range(random.randint(5, 12)):
        port = random.randint(20, 9000)
        state = "open" if random.random() > 0.7 else "closed"
        print_slow(f"  Port {port}: {state}")

def map_network():
    print_slow("Mapping local network...")
    for _ in range(8):
        fake_ip = ".".join(str(random.randint(1,254)) for _ in range(4))
        print_slow(f"  Detected node: {fake_ip}")

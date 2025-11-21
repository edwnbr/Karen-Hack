import random
from .utils import print_slow

def deep_scan(ip):
    print_slow(f"Deep port scan on {ip}...")
    for port in random.sample(range(1, 65535), 30):
        if random.random() > 0.85:
            print_slow(f"  [+] Service detected on {port}")
        else:
            print_slow(f"  [-] {port}/tcp closed")

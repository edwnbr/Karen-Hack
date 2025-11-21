import random
from .utils import print_slow

def hijack(ip):
    print_slow(f"Attempting camera feed access for {ip}...")
    print_slow("  Negotiating stream keys...")
    print_slow("  Access token received.")
    print_slow("  Feed link established (encrypted).")

import random
from .utils import print_slow

def start():
    print_slow("Decrypting intercepted data stream...")
    for _ in range(25):
        chunk = "".join(random.choice("0123456789ABCDEF") for _ in range(32))
        print_slow(f"  {chunk}", 0.0005)
    print_slow("Decryption complete.")

import random
from .utils import print_slow

def dump():
    print_slow("Capturing Wi-Fi broadcast packets...")
    for _ in range(15):
        frame = "".join(random.choice("0123456789ABCDEF") for _ in range(48))
        print_slow(f"  Frame: {frame}")
    print_slow("Capture complete.")

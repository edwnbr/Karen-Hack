import random
from .utils import print_slow

def dump():
    print_slow("Collecting system metadata...")
    print_slow(f"  CPU: EPYC {random.randint(7000, 9000)}")
    print_slow(f"  RAM: {random.randint(8,256)} GB")
    print_slow(f"  Load: {round(random.uniform(0.1, 4.9), 2)}")
    print_slow(f"  Secure keys: extracted")

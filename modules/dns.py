from .utils import print_slow

def poison(ip):
    print_slow(f"Injecting DNS override for {ip}...")
    print_slow("  Hijacking DNS cache...")
    print_slow("  Overwrite successful.")

import random
from .utils import print_slow

def attack(user):
    print_slow(f"Starting authentication attempts for user '{user}'...")
    for _ in range(random.randint(10, 30)):
        pwd = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(6))
        print_slow(f"   Trying: {pwd}")
    print_slow("   Access granted.\n")

import random
from .utils import print_slow

def watch():
    print_slow("Reading recent log entries...")
    for _ in range(20):
        print_slow(f"[LOG] event={random.randint(1000,9999)} status=ok")

def session_spy():
    print_slow("Inspecting active session tokens...")
    for _ in range(6):
        tok = "".join(random.choice("0123456789ABCDEF") for _ in range(32))
        print_slow(f"  token: {tok}")

def task_queue():
    print_slow("Active tasks:")
    items = ["network sweep", "packet capture", "service probe", "credential extraction"]
    for i in items:
        print_slow(f"  • {i} - running")

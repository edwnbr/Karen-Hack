import time
import sys
import random

def type_print(text, speed=0.0015):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def boot_screen():
    lines = [
        "Initializing secure modules...",
        "Loading kernel interfaces...",
        "Activating network stack...",
        "Establishing encrypted shell...",
        "System ready.\n"
    ]
    for line in lines:
        type_print(line, 0.002)
        time.sleep(0.2)

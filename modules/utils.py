import time, random, sys

def print_slow(text, speed=0.001):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
    print()

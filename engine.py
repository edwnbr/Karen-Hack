import os
from commands import execute_command
from hud import type_print, boot_screen


def run_terminal():
    os.system("clear")
    boot_screen()

    while True:
        try:
            cmd = input("$ ")
            execute_command(cmd)
        except KeyboardInterrupt:
            type_print("\nSession terminated.")
            break

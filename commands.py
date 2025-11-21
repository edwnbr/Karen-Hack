from modules import net, ports, bruteforce, decrypt, dns, mitm, wifi, cameras, sysinfo, logs
from hud import type_print


def execute_command(cmd):
    if cmd.startswith("scan --ip"):
        ip = cmd.split()[-1]
        net.scan(ip)

    elif cmd.startswith("deep-scan --ip"):
        ip = cmd.split()[-1]
        ports.deep_scan(ip)

    elif cmd.startswith("bruteforce --user"):
        user = cmd.split()[-1]
        bruteforce.attack(user)

    elif cmd.startswith("decrypt --stream"):
        decrypt.start()

    elif cmd.startswith("dns-poison"):
        ip = cmd.split()[-1]
        dns.poison(ip)

    elif cmd.startswith("mitm --target"):
        ip = cmd.split()[-1]
        mitm.intercept(ip)

    elif cmd.startswith("cam-hijack --ip"):
        ip = cmd.split()[-1]
        cameras.hijack(ip)

    elif cmd == "wifi-dump":
        wifi.dump()

    elif cmd == "sys-dump":
        sysinfo.dump()

    elif cmd == "log-watch":
        logs.watch()

    elif cmd == "net-map":
        net.map_network()

    elif cmd == "session-spy":
        logs.session_spy()

    elif cmd == "task-queue":
        logs.task_queue()

    elif cmd == "clear":
        print("\033[H\033[J", end="")

    elif cmd == "help":
        type_print("""
Available commands:
  scan --ip <ip>
  deep-scan --ip <ip>
  bruteforce --user <name>
  decrypt --stream
  dns-poison <ip>
  mitm --target <ip>
  cam-hijack --ip <ip>
  wifi-dump
  sys-dump
  log-watch
  net-map
  session-spy
  task-queue
""")

    elif cmd == "exit":
        type_print("Session closed.")
        exit()

    else:
        type_print("Unknown command.")

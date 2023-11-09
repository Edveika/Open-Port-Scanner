from PortScanner import PortScanner
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: PortScanner.py IP_ADDRESS")
        return
    
    try:
        scanner = PortScanner(sys.argv[1])
        print(scanner.get_open_ports())
    except Exception as e:
        print(e)

main()
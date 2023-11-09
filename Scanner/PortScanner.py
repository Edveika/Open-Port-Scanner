from CommonPorts import COMMON_PORTS
import requests
import socket

class PortScanner:
    def __init__(self, ip_address):
        # Will contain a list of open ports of selected ip address
        self.open_ports: list[int] = []

        # Checks if user is connected to the internet
        if not self.check_internet_connection():
            raise Exception("No internet connection")
        
        # Checks if the ip address is valid
        if not self.valid_ip(ip_address):
            raise Exception("IP address invalid")
        
        # Gets a list of open ports of selected ip address
        self.retrieve_open_ports(ip_address)
        
    # Pings google to check if user has internet access
    # Returns true if user is connected to the internet
    # False if the user is not connected to the internet
    def check_internet_connection(self) -> bool:
        try:
            response = requests.get("http://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    # Checks if given ip address is valid
    def valid_ip(self, ip_adress):
        try:
            socket.inet_aton(ip_adress)
            return True
        except socket.error:
            return False

    # Checks if port of ip address is open
    # Returns true if open
    # False if not open
    def port_is_open(self, ip_address, port) -> bool:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
    
        result = sock.connect_ex((ip_address, port))
        sock.close()

        if result == 0:
            return True
        
        return False
    
    # Iterates over a list of common ports and checks if any of them are open
    # If there are open ports, adds them to a list
    def retrieve_open_ports(self, ip_address):
        for port in COMMON_PORTS:
            if self.port_is_open(ip_address, port):
                self.open_ports.append(port)

    # Returns a list of open ports
    def get_open_ports(self):
        return self.open_ports
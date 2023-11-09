COMMON_PORTS: list[int] = [
    80,     # HTTP
    443,    # HTTPS
    20,     # FTP (data)
    21,     # FTP (control)
    22,     # SSH
    25,     # SMTP
    53,     # DNS
    67,     # DHCP (server)
    68,     # DHCP (client)
    69,     # TFTP
    23,     # Telnet
    161,    # SNMP
    162,    # SNMP (trap)
    3389,   # RDP
    445,    # SMB
    143,    # IMAP
    110,    # POP3
    389,    # LDAP
    123,    # NTP
    8080,   # HTTP Alt.
    3306,   # MySQL
    5432,   # PostgreSQL
    5900    # VNC
]
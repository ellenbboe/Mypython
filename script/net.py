#!/usr/bin/env python3
import socket


def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
a = socket.getfqdn("8.8.8.8")
print(ip)
print(getip())

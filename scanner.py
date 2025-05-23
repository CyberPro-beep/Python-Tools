#!/usr/bin/python

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.settimeout(1)

host = input("[*] Enter the IP address of system you want to scan it's port: ")
port = int(input("[*] Enter the port to scan: "))

def port_scanner(port):
    if connection.connect_ex((host, port)):
        print(f"Port {port} is Closed")
    else:
        print(f"Port {port} is opened")
    connection.close()

port_scanner(port)
#!/usr/bin/python

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.settimeout(1)

host = "192.168.100.68"
port = 40

def port_scanner(port):
    if connection.connect_ex((host, port)):
        print(f"Port {port} is Closed")
    else:
        print(f"Port {port} is opened")
    connection.close()

port_scanner(port)
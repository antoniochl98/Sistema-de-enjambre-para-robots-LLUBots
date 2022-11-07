#!/usr/bin/env python3

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP


client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 37020))
while True:
    data, addr = client.recvfrom(1024)
    message = data.decode('utf-8')
    instruction = message[0:4]
    limit = message[4:8]
    first_val = message[8:16]
    second_val = message[16:24]
    check_sum = message[24]
    print("received message from %s: %s" % addr, instruction)
#!/bin/bash/env python3

# UDP Client Tool

import socket

target_host = '127.0.0.1'      # Target IP here
target_port = 8080             # Target port 

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data
client.sendto(b"AAABBBCCC",(target_host,target_port))

# Receive data
data, addr = client.recvfrom(4096)

# Print out the response
print(data.decode())
client.close()
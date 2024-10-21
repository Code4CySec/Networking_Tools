#!/bin/bash/env python3

# TCP Client Tool

import socket

target_host = 'www.example.com'    # Target website or IP here
target_port = 80                   # Target port 

# Create a socket object
client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive data
response = client.recv(4096)

# Print out the response
print(response.decode())
client.close()
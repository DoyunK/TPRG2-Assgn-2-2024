#Doyun Kim (100924397)
#Client

import socket
import json

# Create a socket object and connect to the server
s = socket.socket()
host = '192.168.10.111'  # Replace with your Raspberry Pi's IP address
port = 5000
s.connect((host, port))

# Receive data from the server
data = s.recv(1024).decode('utf-8')  # Decode the received bytes into a string
s.close()

# Parse the JSON data and print each key-value pair
data_dict = json.loads(data)
for key, value in data_dict.items():
    print(f"{key}: {value}")

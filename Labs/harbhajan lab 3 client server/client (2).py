#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:19:49 2023

@author: bhajji
"""
#Importing important packages
import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (replace 'localhost' and '8080' with the server's IP address and port)
server_address = ('localhost', 8080)
client_socket.connect(server_address)

try:
    while True:
        # Input a command from the user
        command = input("Enter a command (TIME/EXIT): ").strip()

        # Send the command to the server
        client_socket.send(command.encode())

        if command == "EXIT":
            break

        # Receive and print the server's response
        response = client_socket.recv(1024).decode()
        print(response)

finally:
    client_socket.close()

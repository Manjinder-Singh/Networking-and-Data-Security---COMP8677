#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:19:49 2023

@author: bhajji
"""
#Importing important packages
import socket
import time

# Function to handle client connections
def handle_client(client_socket):
    try:
        # Send the client's IP address and port number
        client_address = client_socket.getpeername()
        client_socket.send(f"Connected to {client_address}\n".encode())

        # Set a timeout for the client socket (15 seconds)
        client_socket.settimeout(15)

        while True:
            # Receive a command from the client
            command = client_socket.recv(1024).decode().strip()

            if not command:
                break

            if command == "TIME":
                # Get the current time and send it to the client
                current_time = time.ctime()
                client_socket.send(current_time.encode())
            elif command == "EXIT":
                # Close the client socket and exit the loop
                break
            else:
                # Invalid command, send an error message
                client_socket.send("Invalid command!\n".encode())

    except socket.timeout:
        print(f"Client {client_address} timed out")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific host and port
server_socket.bind(("0.0.0.0", 8080))

# Listen for incoming connections (maximum 5 clients in the queue)
server_socket.listen(5)
print("Server listening on port 8080")

try:
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Handle the client in a separate thread or process for concurrent connections
        handle_client(client_socket)

except KeyboardInterrupt:
    print("Server shutting down")
finally:
    server_socket.close()

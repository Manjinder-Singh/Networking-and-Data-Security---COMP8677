"""
Name - Manjinder Singh
Student ID - 110097177
Subject - Networking and Data Security
Class Day - Monday
Lab - 2; Question - 4
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:45:56 2023

@author: Manjinder Singh
"""

"""
# Package import for socket library.
import socket

def clientFunctionality():
    # Firstly, we will be creating a Transmission Control Protocol(TCP) socket.
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Secondly, we will be connecting to the server (we can update the IP and Port number as per server, using localhost in our case.)
    serverAddr = ('localhost', 8080)
    tcpSocket.connect(serverAddr)

    try:
        while True:
            # Taking a I/P command from the end-user.
            ipCmd = input("Please enter command from either TIME or EXIT:- ").strip()

            # Now, sending the command to the server.
            tcpSocket.send(ipCmd.encode())

            if ipCmd == "EXIT":
                break

            # Finally, receiving and printing the server's response
            response = tcpSocket.recv(1024).decode()
            print("Received Response:- ",response)

    finally:
        tcpSocket.close()

if __name__ == '__main__':
    clientFunctionality()
    
    
    """
import socket

def clientFunctionality():
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddr = ('localhost', 8080)

    try:
        tcpSocket.connect(serverAddr)

        # Receive and print the initial connection message from the server
        initial_message = tcpSocket.recv(1024).decode()
        print(initial_message)

        while True:
            ipCmd = input("Please enter a command (TIME or EXIT): ").strip()

            tcpSocket.send(ipCmd.encode())

            if ipCmd == "EXIT":
                break

            response = tcpSocket.recv(1024).decode()
            print("Received Response:", response)
            
        # Adding a pause so that before exiting and to keep the console OPEN.
        input("Press Enter for final exit from console...")

    finally:
        tcpSocket.close()

if __name__ == '__main__':
    clientFunctionality()


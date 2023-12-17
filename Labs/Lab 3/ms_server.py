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
Created on Mon Sep 18 18:00:07 2023

@author: Manjinder Singh
"""

# Package import for socket and time library.
import socket
import time

import socket
import time

def clientCmds(clientSock, clientAddr):
    try:
        clientSock.send(f"We are now connected to {clientAddr}\n".encode())

        clientSock.settimeout(15)

        while True:
            recCmd = clientSock.recv(1024).decode().strip()

            if not recCmd:
                break

            if recCmd == "TIME":
                currTime = time.ctime()
                clientSock.send(currTime.encode())
            elif recCmd == "EXIT":
                break
            else:
                clientSock.send("Invalid command entered!\n".encode())

    except socket.timeout:
        print(f"Client at {clientAddr} timed out.")
    except Exception as e:
        print(f"ISSUE ENCOUNTERED: An error occurred: {e}")
    finally:
        clientSock.close()

def serverFunctionality():
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock.bind(('0.0.0.0', 8080))
    serverSock.listen(5)  # Allow up to 5 clients to wait in the queue

    print("Server started & listening on port 8080.\n")

    try:
        while True:
            clientSock, clientAddr = serverSock.accept()
            print(f"Connection is accepted from {clientAddr}")
            clientCmds(clientSock, clientAddr)
    except KeyboardInterrupt:
        print("Server connection is shutting down...")
    finally:
        serverSock.close()

if __name__ == "__main__":
    serverFunctionality()


#!/usr/bin/python3

import socket, ssl, sys, pprint

hostname = sys.argv[1]
port = 4433
cadir = '/volumes/certC'

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_verify_locations(capath=cadir)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True

def messageSendRec(client_socket, message):
    my_socket = context.wrap_socket(client_socket, server_hostname=hostname, do_handshake_on_connect=False)
    my_socket.do_handshake()

    my_socket.sendall(message.encode())
    response = my_socket.recv(2048).decode()
    print(f"Received Response:- {response}") #Printing received response.

    my_socket.shutdown(socket.SHUT_RDWR)
    my_socket.close() #Closing socket connection.

while True:
    input_message = input("Please enter message (or enter 'exit' to quit):- ")
    if input_message.lower() == 'exit':
        break

    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Host Name-", hostname)
    my_sock.connect((hostname, port))
    messageSendRec(my_sock, input_message)

print("Client is now exiting...")

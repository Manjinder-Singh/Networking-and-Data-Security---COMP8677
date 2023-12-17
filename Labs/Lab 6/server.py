# !/usr/bin/python3

import socket
import ssl
import pprint
import threading

html = """
HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
"""

SERVER_CERT = '/volumes/certS/Test.crt'
SERVER_PRIVATE = '/volumes/certS/Test.key'

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(SERVER_CERT, SERVER_PRIVATE)

def client_handler(client_socket):
    try:
        my_socket = context.wrap_socket(client_socket, server_side=True)
        print("TLS connection established successfully.")

        while True:
            data = my_socket.recv(1024)  # Reading data with TLS connection.
            if not data:
                break

            reversed_data = data[::-1].decode('utf-8')
            print(f"Received Response:- {data.decode('utf-8')}")
            print(f"Reversed Response:- {reversed_data}")

            # Sending the reversed message to the client.
            my_socket.sendall(reversed_data.encode())

        my_socket.shutdown(socket.SHUT_RDWR)  # Using shutdown to close the TLS connection.
        my_socket.close()
    except Exception:
        print("Exception Occured: TLS connection unsuccessful.")


my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
my_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# my_sock.bind(('10.0.2.15', 4433))
my_sock.bind(('10.9.0.5', 4433))
my_sock.listen(5)

while True:
    newsock, fromaddr = my_sock.accept()
    # print("TCP connection is still successfully.")

    myClientThread = threading.Thread(target=client_handler, args=(newsock,))
    myClientThread.start()

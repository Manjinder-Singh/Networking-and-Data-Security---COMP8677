import socket
import time

def handle_client(client_socket, client_address):
    client_socket.send(f"Connected to server. Your IP address and port are: {client_address}\n".encode())

    while True:
        try:
            command = client_socket.recv(1024).decode().strip()
            if not command:
                break

            if command == "TIME":
                current_time = time.ctime()
                client_socket.send(f"{current_time}\n".encode())

            elif command == "EXIT":
                client_socket.close()
                return "EXIT"

            else:
                client_socket.send("Invalid command!\n".encode())

        except socket.timeout:
            break

    client_socket.close()

def main():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ss.bind(('', 4000))
    ss.listen(1)

    print("Server started, waiting for connections...")
    
    try:
        while True:
            client_socket, client_address = ss.accept()
            client_socket.settimeout(15)
            
            response = handle_client(client_socket, client_address)
            if response == "EXIT":
                break

    finally:
        ss.close()

if __name__ == "__main__":
    main()

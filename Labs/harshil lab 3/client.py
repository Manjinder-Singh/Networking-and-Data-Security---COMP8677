import socket

def main():
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    server_address = ('', 4000)
    s.connect(server_address)

    print(s.recv(1024).decode())  # Print the welcome message from the server

    try:
        while True:
            # Send data to the server
            message = input("Enter command (TIME/EXIT/other): ")
            if not message:
                break

            s.sendall(message.encode())
            
            # Receive and print server response
            response = s.recv(1024)
            print(response.decode())
            
            if message == "EXIT":
                break

    finally:
        s.close()

if __name__ == '__main__':
    main()
